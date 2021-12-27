
def solution(M, F):

    def gcd(p, q):
        c = 0

        while q != 0:
            c += p // q
            p, q = q, p % q

        return p, c - 1

    p, c = gcd(int(M), int(F))

    return str(c) if p == 1 else "impossible"
