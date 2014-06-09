def solution(A, B):
    stack = [-1] # non-eaten downwarders
    alive = 0
    for fish, flow in zip(A, B):
        if flow == 1:
            stack.append(fish)
            continue
        while stack[-1] != -1:
            if stack[-1] < fish:
                stack.pop()
            else:
                break
        else:
            alive += 1
            
    return len(stack) + alive - 1 
