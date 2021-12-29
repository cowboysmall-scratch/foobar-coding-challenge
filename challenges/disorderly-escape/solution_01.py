
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


    def cycle_combinations_rec(i, n, l, c, t = []):
        if n == 0:
            c.append(list(Counter(t[:l]).items()))

        for j in range(i, n + 1):
            t.append(j)
            cycle_combinations_rec(j, n - j, l + 1, c, t)
            t.pop()


    def cycle_combinations(n):
        c = []
        cycle_combinations_rec(1, n, 0, c)
        return c


    def get_coefficient(cycle):
        coefficient = 1
        for v, f in cycle:
            coefficient *= factorial(f)
            coefficient *= v**f
        return coefficient


    rows = [(cycle, get_coefficient(cycle)) for cycle in cycle_combinations(h)]
    cols = [(cycle, get_coefficient(cycle)) for cycle in cycle_combinations(w)]

    count = 0

    for row_cycle, row_coefficient in rows:
        for col_cycle, col_coefficient in cols:
            total = 1
            for v1, f1 in row_cycle:
                for v2, f2 in col_cycle:
                    exp    = (v1 * f1 * v2 * f2) // lcm(v1, v2)
                    total *= s**exp

            count += Fraction(total, col_coefficient * row_coefficient)

    return str(count)
