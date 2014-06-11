def solution(A):
    diff = curr_max = 0
    curr_min = 200000
    for value in A:
        if value < curr_min:
            curr_min = value
            curr_max = 0
        elif value > curr_max:
            curr_max = value
            if curr_max - curr_min > diff:
                diff = curr_max - curr_min
    
    return diff
