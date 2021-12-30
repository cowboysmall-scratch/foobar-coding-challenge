
def solution(s):
    return ''.join([chr(219 - ord(c)) if 97 <= ord(c) <= 122 else c for c in s])
