
from collections import deque


def solution(map):
    h = len(map)
    w = len(map[0])
    b = 1

    G = [[[c] * (b + 1) for c in r] for r in map]
    D = [(1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0), (1, 0, 1), (0, 1, 1), (-1, 0, 1), (0, -1, 1)]

    V = set([(0, 0, 0)])
    Q = deque([(0, 0, 0, 1)])

    while Q:
        i, j, k, l = Q.popleft()

        if (i, j) == (h - 1, w - 1):
            return l

        for dx, dy, dz in D:
            di, dj, dk = i + dx, j + dy, k + dz
            if 0 <= di < h and 0 <= dj < w and 0 <= dk < b + 1 and (di, dj, dk) not in V:
                if k == dk and G[di][dj][dk] == 0 or k < dk and G[di][dj][dk] == 1:
                    V.add((di, dj, dk))
                    Q.append((di, dj, dk, l + 1))

    return -1
