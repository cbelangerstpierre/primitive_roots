import math
import timeit

import numpy
import sympy


def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n // 3 + (n % 6 == 2), dtype=bool)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = False
    return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]


def onlyTest(mod):
    mod_minus1 = mod - 1
    generators = list()
    tests = list(map(lambda x: int(mod_minus1 / x), sympy.primefactors(mod_minus1)))
    for a in range(1, mod):
        if math.isqrt(a) ** 2 == a:
            continue
        is_valid = True
        for test in tests:
            if pow(a, test, mod) == 1:
                is_valid = False
                break
        if is_valid:
            generators.append(a)
    return generators


def testAndMGenerate(mod):
    mod_minus1 = mod - 1
    generators = list()
    first_a = 0
    tests = list(map(lambda x: int(mod_minus1 / x), sympy.primefactors(mod_minus1)))
    for a in range(1, mod):
        if math.isqrt(a) ** 2 == a:
            continue
        is_valid = True
        for test in tests:
            if pow(a, test, mod) == 1:
                is_valid = False
                break
        if is_valid:
            first_a = a
            break
    for m in range(1, mod):
        if math.gcd(m, mod - 1) == 1:
            generators.append(pow(first_a, m, mod))
    generators.sort()
    return generators


start = timeit.default_timer()
for q in list(map(int, primesfrom2to(2000))):
    result = onlyTest(q)
    # print(q, "->", result)
print("Time :", timeit.default_timer() - start)

start = timeit.default_timer()
for q in list(map(int, primesfrom2to(2000))):
    result = testAndMGenerate(q)
    # print(q, "->", result)
print("Time :", timeit.default_timer() - start)
