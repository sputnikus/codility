def solution(X, A):
    cov_time = [-1] * X
    uncovered = X
    
    for t, pos in enumerate(A):
        if cov_time[pos-1] == -1:
            cov_time[pos-1] = t
            uncovered -= 1
            if uncovered == 0:
                return t
    return -1
