def solution(S):
    opening  = '([{'
    closing = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    stack = []
    
    for x in S:
        if x in opening:
            stack.append(x)
            continue
        if len(stack) == 0:
            return 0
        if closing[x] != stack.pop():
            return 0
            
    if len(stack) == 0:
        return 1
    return 0
