import math
import timeit

import numpy
import sympy


def onlyTest(mod):
    return [a for a in range(1, mod) if math.isqrt(a) ** 2 != a and all(pow(a, test, mod) != 1 for test in list(map(lambda x: (mod - 1) // x, sympy.primefactors(mod - 1))))]


def testAndMGenerate(mod):
    for a in range(1, mod):
        if math.isqrt(a) ** 2 != a and all(pow(a, test, mod) != 1 for test in list(map(lambda x: (mod - 1) // x, sympy.primefactors(mod - 1)))):
            return sorted([pow(a, m, mod) for m in range(1, mod) if math.gcd(m, mod - 1) == 1])


def primesfrom2to(n):
    sieve = numpy.ones(n // 3 + (n % 6 == 2), dtype=bool)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = False
    return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]


start = timeit.default_timer()
for q in list(map(int, primesfrom2to(200))):
    result = onlyTest(q)
    print(q, "->", result)
print("Time :", timeit.default_timer() - start)

start = timeit.default_timer()
for q in list(map(int, primesfrom2to(200))):
    result = testAndMGenerate(q)
    print(q, "->", result)
print("Time :", timeit.default_timer() - start)
