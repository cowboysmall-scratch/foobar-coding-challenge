
from collections import deque


def solution(map):

    def shortest_path(map, s, e):
        G = [[[c] * (g + 1) for c in r] for r in map]
        d = [(0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0), (0, -1, 1), (0, 1, 1), (-1, 0, 1), (1, 0, 1)]

        V = set([s])
        Q = deque([(s[0], s[1], s[2], 1)])


        while Q:
            i, j, k, l = Q.popleft()

            if (i, j, k) == e:
                return l

            for dx, dy, dz in d:
                di, dj, dk = i + dx, j + dy, k + dz
                if 0 <= di < h and 0 <= dj < w and 0 <= dk < g + 1:
                    if (di, dj, dk) not in V:
                        if k == dk and G[di][dj][dk] == 0 or k < dk and G[di][dj][k] == 1:
                            V.add((di, dj, dk))
                            Q.append((di, dj, dk, l + 1))

        return -1


    h = len(map)
    w = len(map[0])
    g = 1

    return shortest_path(map, (0, 0, 0), (h - 1, w - 1, g))
