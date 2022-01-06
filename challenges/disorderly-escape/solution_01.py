
from math        import factorial
from fractions   import Fraction
from collections import Counter


def solution(w, h, s):
    total = 0


    def gcd(p, q):
        while q:
            p, q = q, p % q
        return p

    def cycles(n):
        c = []

        def cycles_rec(i, n, l, t = []):
            if n == 0:
                c.append(list(Counter(t[:l]).items()))

            for j in range(i, n + 1):
                t.append(j)
                cycles_rec(j, n - j, l + 1, t)
                t.pop()

        cycles_rec(1, n, 0)

        return c

    def denom(c):
        d = 1
        for v, f in c:
            d *= v**f * factorial(f)
        return d

    def exponent(c1, c2):
        e = 0
        for v1, f1 in c1:
            for v2, f2 in c2:
                e += f1 * f2 * gcd(v1, v2)
        return e


    row_cycles = cycles(h)
    col_cycles = cycles(w)

    row_denoms = [denom(rc) for rc in row_cycles]
    col_denoms = [denom(cc) for cc in col_cycles]

    for row_cycle, row_denom in zip(row_cycles, row_denoms):
        for col_cycle, col_denom in zip(col_cycles, col_denoms):
            total += Fraction(s**exponent(row_cycle, col_cycle), row_denom * col_denom)

    return str(total)
