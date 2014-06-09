def solution(H):
    stack = [0]
    rects = 0
    
    for height in H:
        if height > stack[-1]:
            stack.append(height)
            rects += 1
        elif height < stack[-1]:
            while height < stack[-1]:
                stack.pop()
                if height == stack[-1]:
                    break
            else:
                stack.append(height)
                rects += 1
    return rects
