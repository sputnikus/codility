def solution(N, P, Q):
    half = (N // 2) + 1
    sieve = [True] * half
    for i in xrange(3,int(half**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((half-i*i-1)/(2*i)+1)
    primes = [2] + [i for i in xrange(3,half,2) if sieve[i]]
    primes_count = len(primes)
    semiprimes = [0] * (N + 1)
    for x in xrange(primes_count - 1):
        for y in xrange(x, primes_count):
            if primes[x] * primes[y] > N:
                break
            semiprimes[primes[x] * primes[y]] = 1
    for i in xrange(1, N + 1):
        semiprimes[i] += semiprimes[i-1]
    results = []
    for start, stop in zip(P, Q):
        results.append(semiprimes[stop] - semiprimes[start - 1])
    return results
