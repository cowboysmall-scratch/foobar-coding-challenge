
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

    def denominator(c):
        d = 1
        for v, f in c:
            d *= v**f * factorial(f)
        return d

    def exponent(c1, c2):
        n = 0
        for v1, f1 in c1:
            for v2, f2 in c2:
                n += f1 * f2 * gcd(v1, v2)
        return n


    for row_cycle in cycles(h):
        for col_cycle in cycles(w):
            total += Fraction(s**exponent(row_cycle, col_cycle), denominator(row_cycle) * denominator(col_cycle))

    return str(total)
