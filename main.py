import math
import timeit

import numpy
import sympy


# start = timeit.default_timer()
# for q in range(2, 250):
#     generators = list()
#     for a in range(1, q):
#         numbers = set()
#         for i in range(1, q):
#             numbers.add((a ** i) % q)
#         if len(numbers) == q - 1:
#             generators.append(a)
#     if len(generators) != 0:
#         print(q, "->", generators)
# print("Time :", timeit.default_timer() - start)
# print(pow(11, 23, 47))
# print(pow(147, 380, 761))

# for i in range(2, 761):
#     if pow(i, 380, 761) == :
#         print(i)
# print(pow(2937, 760, 761))


# for q in range(3, 50):
#     generators = list()
#     q_minus1 = q-1
#     q_minus1_divided2 = int(q_minus1 / 2)
#     for a in range(1, q):
#         # print(a, q_minus1_divided2, q_minus1)
#         # print(pow(a, q_minus1_divided2, q_minus1))
#         if pow(a, q_minus1_divided2, q) == q_minus1:
#             generators.append(a)
#     if len(generators) != 0:
#         print(q, "->", generators)


# for i in range(1, 7):
#     print(pow(6, i, 7))
#
# print()
# print(pow(6, 3, 7))


def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n // 3 + (n % 6 == 2), dtype=bool)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = False
    return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]


start = timeit.default_timer()
for q in list(map(int, primesfrom2to(2000))):
    q_minus1 = q - 1
    generators = list()
    for a in range(1, q):
        if math.isqrt(a) ** 2 == a:
            continue
        tests = list(map(lambda x: int(q_minus1 / x), sympy.primefactors(q_minus1)))
        is_valid = True
        for test in tests:
            if pow(a, test, q) == 1:
                is_valid = False
                break
        if is_valid:
            generators.append(a)
    if len(generators) != 0:
        print(q, "->", generators)
print("Time :", timeit.default_timer() - start)


# start = timeit.default_timer()
# for q in list(map(int, primesfrom2to(2000))):
#     q_minus1 = q - 1
#     generators = list()
#     first_a = 0
#     for a in range(1, q):
#         if math.isqrt(a) ** 2 == a:
#             continue
#         tests = list(map(lambda x: int(q_minus1 / x), sympy.primefactors(q_minus1)))
#         is_valid = True
#         for test in tests:
#             if pow(a, test, q) == 1:
#                 is_valid = False
#                 break
#         if is_valid:
#             first_a = a
#             break
#     for m in range(1, q):
#         if sympy.gcd(m, q - 1) == 1:
#             generators.append(pow(first_a, m, q))
#     generators.sort()
#     print(q, "->", generators)
# print("Time :", timeit.default_timer() - start)



# print(sympy.gcd(46, 84))
# q = 29
# generators = list()
# for m in range(1, q):
#     if sympy.gcd(m, q-1) == 1:
#         generators.append(pow(2, m, q))
# generators.sort()
# print(generators)

