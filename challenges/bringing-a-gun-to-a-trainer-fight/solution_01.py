
from math import atan2


def solution(dimensions, your_position, trainer_position, distance):
    w, h = dimensions
    x, y = your_position
    a, b = trainer_position

    m_x  = ((x + distance) // w) + 1
    m_y  = ((y + distance) // h) + 1

    dd   = distance**2


    def reflect(x1, y1, n, m):
        return (n * w) + (w - x1) if n % 2 == 1 else (n * w) + x1, (m * h) + (h - y1) if m % 2 == 1 else (m * h) + y1

    def l2(x1, y1):
        return (x1 - x)**2 + (y1 - y)**2

    def angle(x1, y1):
        return atan2((y1 - y), (x1 - x))


    pp1 = []
    for i in range(m_x + 1):
        for j in range(m_y + 1):
            p = reflect(x, y, i, j)
            if l2(*p) <= dd:
                pp1.append((p[0], p[1], 0))

            p = reflect(a, b, i, j)
            if l2(*p) <= dd:
                pp1.append((p[0], p[1], 1))


    pp2 = [(-p[0],  p[1], p[2]) for p in pp1 if l2(-p[0],  p[1]) <= dd]
    pp3 = [(-p[0], -p[1], p[2]) for p in pp1 if l2(-p[0], -p[1]) <= dd]
    pp4 = [( p[0], -p[1], p[2]) for p in pp1 if l2( p[0], -p[1]) <= dd]


    aa = {}
    for p in pp1:
        d = l2(p[0], p[1])
        a = angle(p[0], p[1])
        if d > 0 and (a not in aa or d < aa[a][3]):
            aa[a] = (p[0], p[1], p[2], d)

    for p in pp2:
        d = l2(p[0], p[1])
        a = angle(p[0], p[1])
        if d > 0 and (a not in aa or d < aa[a][3]):
            aa[a] = (p[0], p[1], p[2], d)

    for p in pp3:
        d = l2(p[0], p[1])
        a = angle(p[0], p[1])
        if d > 0 and (a not in aa or d < aa[a][3]):
            aa[a] = (p[0], p[1], p[2], d)

    for p in pp4:
        d = l2(p[0], p[1])
        a = angle(p[0], p[1])
        if d > 0 and (a not in aa or d < aa[a][3]):
            aa[a] = (p[0], p[1], p[2], d)


    c = 0
    for _, v in aa.iteritems():
        if v[2] == 1:
            c += 1

    return c

