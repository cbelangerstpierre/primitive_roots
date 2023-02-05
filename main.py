import math
import timeit
import numpy
import sympy


def onlyTest(mod):
    mod_minus1 = mod - 1
    tests = list(map(lambda x: mod_minus1 // x, sympy.primefactors(mod_minus1)))
    return [a for a in range(1, mod) if math.isqrt(a) ** 2 != a and all(pow(a, test, mod) != 1 for test in tests)]


def testAndMGenerate(mod):
    mod_minus1 = mod - 1
    for a in range(1, mod):
        tests = list(map(lambda x: mod_minus1 // x, sympy.primefactors(mod_minus1)))
        if math.isqrt(a) ** 2 != a and all(pow(a, test, mod) != 1 for test in tests):
            return sorted([pow(a, m, mod) for m in range(1, mod) if math.gcd(m, mod_minus1) == 1])


def primesfrom2to(n):
    sieve = numpy.ones(n // 3 + (n % 6 == 2), dtype=bool)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = False
    return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]


def test_function(function):
    start = timeit.default_timer()
    for q in list(map(int, primesfrom2to(20000))):
        result = function(q)
        # print(q, "->", result)
    print("Time :", timeit.default_timer() - start)


test_function(onlyTest)
test_function(testAndMGenerate)
