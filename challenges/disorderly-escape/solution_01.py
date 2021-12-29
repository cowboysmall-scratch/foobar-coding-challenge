
from math        import factorial
from fractions   import Fraction
from collections import Counter


def solution(w, h, s):

    def gcd(p, q):
        while q:
            p, q = q, p % q
        return p

    def lcm(p, q):
        return p * q // gcd(p, q)

    def cycle_combs(n):
        c = []
        cycle_combs_rec(1, n, 0, c)
        return c

    def cycle_combs_rec(i, n, l, c, t = []):
        if n == 0:
            c.append(list(Counter(t[:l]).items()))

        for j in range(i, n + 1):
            t.append(j)
            cycle_combs_rec(j, n - j, l + 1, c, t)
            t.pop()

    def calc_coeff(c):
        cf = 1
        for v, f in c:
            cf *= v**f
            cf *= factorial(f)
        return cf


    row_cycles = cycle_combs(h)
    col_cycles = cycle_combs(w)
    row_coeffs = [calc_coeff(c) for c in row_cycles]
    col_coeffs = [calc_coeff(c) for c in col_cycles]

    total = 0

    for row_cycle, row_coeff in zip(row_cycles, row_coeffs):
        for col_cycle, col_coeff in zip(col_cycles, col_coeffs):
            term = Fraction(1, col_coeff * row_coeff)
            for v1, f1 in row_cycle:
                for v2, f2 in col_cycle:
                    exp   = (v1 * f1 * v2 * f2) // lcm(v1, v2)
                    term *= s**exp
            total += term

    return str(total)
