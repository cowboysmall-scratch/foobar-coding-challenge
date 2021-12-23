
def solution(s):
    count_t = 0
    count_r = 0

    for c in s:
        if c == '>':
            count_r += 2
        if c == '<':
            count_t += count_r

    return count_t
