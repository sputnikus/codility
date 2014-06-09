def solution(S):
    if not S:
        return 1
    input_len = len(S)
    if input_len % 2 != 0:
        return 0
    left = 0
    for paren in S:
        if paren == '(':
            left += 1
        elif paren == ')':
            left -= 1
        if left < 0:
            return 0
    if left == 0:
        return 1
    return 0
