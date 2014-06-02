def solution(A):
    intersects = 0
    a_len = len(A)
    low_bounds = [0] * a_len
    high_bounds = [0] * a_len
    for index in xrange(a_len):
        low_bounds[index] = index - A[index] 
        high_bounds[index] = index + A[index] 
    low_bounds = sorted(low_bounds)
    high_bounds = sorted(high_bounds)
    low_index = 0
    for high_index in xrange(a_len):
        while low_index < a_len and high_bounds[high_index] >= low_bounds[low_index]:
            low_index += 1
        intersects += low_index - high_index - 1
        if intersects > 10000000:
            return -1
    return intersects
