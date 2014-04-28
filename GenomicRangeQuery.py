def solution(S, P, Q):
    impacts = {'A':1, 'C':2, 'G':3, 'T':4,}
    N = len(S)
    M = len(P)
    factor_map = dict((key, [0]*N) for key in impacts)
    
    for i, nucle in enumerate(S):
        factor_map[nucle][i] += 1
        if i < N - 1:
            for factor in factor_map:
                factor_map[factor][i+1] = factor_map[factor][i]
        
    for j in xrange(M):
        pre_sum = [0] * 4
        if P[j] > 0:
            pre_sum = [pre[P[j]] for pre in factor_map.values()]
        post_sum = [post[Q[j]] for post in factor_map.values()]
        for k in xrange(4):
            if post_sum[k] - pre_sum[k] > 0:
                P[j] = k + 1
                break
        else:
            P[j] = impacts[S[P[j]]]
    return P
