

def solution(h, q):
    root = 2**h - 1

    def process(start, end, parent, value):
        interval = end - start
        if interval == 0:
            return parent
        elif interval == 3:
            if value == start or value == start + 1:
                return end
            else:
                return parent
        else:
            if value == end:
                return parent
            delta = interval // 2
            if start <= value < start + delta:
                return process(start, start + delta - 1, end, value)
            else:
                return process(start + delta, end - 1, end, value)

    return [process(1, root, -1, v) for v in q]

