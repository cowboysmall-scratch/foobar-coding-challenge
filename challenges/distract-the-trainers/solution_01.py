
from collections import defaultdict
from itertools   import combinations


def solution(banana_list):
    loop   = defaultdict(list)
    guards = list(enumerate(banana_list))
    count  = len(guards)


    def gcd(p, q):
        while q:
            p, q = q, p % q
        return p

    def exits(p, q):
        s = (p + q) // gcd(p, q)
        return s & (s - 1) == 0 and s != 0

    def sort_guards():
        guards.sort(key = lambda g: len(loop[g]))

    def get_pair():
        for g in guards[1:]:
            if g in loop[guards[0]]:
                return (guards[0], g)
        return None

    def remove_guard(g):
        for gg in loop[g]:
            loop[gg].remove(g)
        guards.remove(g)

    def remove_pair(p):
        remove_guard(p[0])
        remove_guard(p[1])


    for c in combinations(guards, 2):
        if not exits(c[0][1], c[1][1]):
            loop[c[0]].append(c[1])
            loop[c[1]].append(c[0])


    while len(guards) > 1:

        sort_guards()
        p = get_pair()

        if not p:
            p = (guards[0], guards[1])
        else:
            count -= 2

        remove_pair(p)


    return count