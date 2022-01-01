
def solution(M, F):
    p, q, c = int(M), int(F), 0

    while q != 0:
        c += p // q
        p, q = q, p % q

    return str(c - 1) if p == 1 else "impossible"
