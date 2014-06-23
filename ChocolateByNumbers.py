def solution(N, M):
    a, b = N, M
    while a:
        a, b = b % a, a
    return N // b
