def solution(A):
    a_max, a_len = max(A), len(A)
    if len(set(A)) != a_len or a_max != a_len:
        return 0
    return 1
