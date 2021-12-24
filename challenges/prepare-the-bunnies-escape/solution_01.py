
from collections import deque


def solution(map):

    def shortest_path(G, h, w, s, e):
        d = [(0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0), (0, -1, 1), (0, 1, 1), (-1, 0, 1), (1, 0, 1)]

        V = set([s])
        Q = deque([(*s, 1)])


        while Q:
            i, j, k, l = Q.popleft()

            if i == e[0] and j == e[1] and k == e[2]:
                return l

            for dx, dy, dz in d:
                di, dj, dk = i + dx, j + dy, k + dz
                if 0 <= di < h and 0 <= dj < w and 0 <= dk < 2:
                    if (di, dj, dk) not in V:
                        if k == dk and G[di][dj][dk] == 0 or k == 0 and dk == 1 and G[di][dj][0] == 1:
                            V.add((di, dj, dk))
                            Q.append((di, dj, dk, l + 1))

        return -1


    G    = [[[c, c] for c in r] for r in map]
    h    = len(G)
    w    = len(G[0])

    return shortest_path(G, h, w, (0, 0, 0), (h - 1, w - 1, 1))
