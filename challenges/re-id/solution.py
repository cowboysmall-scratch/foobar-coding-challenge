
def solution(i):

    def primes(n):
        N = n**2
        p = [1] * N

        for j in range(2, n):
            if p[j]:
                for k in range(j**2, N, j):
                    p[k] = 0

        return ''.join([str(l) for l in range(N) if p[l] == 1][2:])

    return primes(143)[i:i + 5]
