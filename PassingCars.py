def solution(A):
    MAX_PASS = 1000000000
    multipler = 1
    passes = 0
    try:
        first_east = A.index(0)
    except ValueError:
        return passes
    for car in A[first_east+1:]:
        if car == 0:
            multipler += 1
            continue
        passes += multipler
        if passes > MAX_PASS:
            return -1
    return passes
