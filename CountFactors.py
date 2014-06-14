def solution(N):
    a, r = 1, [1]
    while a * a < N:
        a += 1
        if N % a:
            continue
        b, f = 1, []
        while N % a == 0:
            N //= a
            b *= a
            f += [i * b for i in r]
        r += f
    if N > 1:
        r += [i * N for i in r]
    return len(r)
