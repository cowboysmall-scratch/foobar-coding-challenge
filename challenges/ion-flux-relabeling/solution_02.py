
def solution(h, q):
    root = 2**h - 1

    def process(start, end, parent, value):
        if value == end:
            return parent

        interval = end - start
        if interval > 2:
            delta = interval // 2
            if start <= value < start + delta:
                return process(start, start + delta - 1, end, value)
            else:
                return process(start + delta, end - 1, end, value)
        else:
            return parent if interval == 0 else end

    return [process(1, root, -1, v) for v in q]
