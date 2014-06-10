def solution(A):
    candidate = 0
    count = 0
    index = -1
    
    for i, value in enumerate(A):
        if count == 0:
            candidate = value
            count += 1
            index = i
        else:
            if value == candidate:
                count += 1
            else:
                count -= 1
                
    if A.count(candidate) <= len(A) // 2:
        return -1
    else:
        return index
