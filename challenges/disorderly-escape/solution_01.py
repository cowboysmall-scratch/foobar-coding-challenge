
from math        import factorial
from fractions   import Fraction
from collections import Counter


def solution(w, h, s):
    total = 0


    def gcd(p, q):
        while q:
            p, q = q, p % q
        return p

    def lcm(p, q):
        return p * q // gcd(p, q)

    def cycles(n):
        c = []
        t = []

        def cycles_rec(i, n, l):
            if n == 0:
                c.append(list(Counter(t[:l]).items()))

            for j in range(i, n + 1):
                t.append(j)
                cycles_rec(j, n - j, l + 1)
                t.pop()

        cycles_rec(1, n, 0)

        return c

    def denominator(c):
        d = 1
        for v, f in c:
            d *= v**f * factorial(f)
        return d

    def numerator(c1, c2, s):
        n = 1
        for v1, f1 in c1:
            for v2, f2 in c2:
                n *= s**((v1 * f1 * v2 * f2) // lcm(v1, v2))
        return n


    row_cycles = cycles(h)
    col_cycles = cycles(w)

    row_denoms = [denominator(rc) for rc in row_cycles]
    col_denoms = [denominator(cc) for cc in col_cycles]

    for row_cycle, row_denom in zip(row_cycles, row_denoms):
        for col_cycle, col_denom in zip(col_cycles, col_denoms):
            total += Fraction(numerator(row_cycle, col_cycle, s), row_denom * col_denom)

    return str(total)
