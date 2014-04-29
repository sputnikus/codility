IMPACTS = {'A':1, 'C':2, 'G':3, 'T':4,}

def solution(S, P, Q):
    N = len(S)
    M = len(P)
    factor_list = [[0]*N for _ in xrange(4)]
    
    for i, nucle in enumerate(S):
        factor_list[IMPACTS[nucle]-1][i] += 1
        if i < N - 1:
            for factor in factor_list:
                factor[i+1] = factor[i]
   
    for j in xrange(M):
        lefty = P[j]
        if lefty == Q[j]:
            P[j] = IMPACTS[S[lefty]]
            continue
        pre_sum = [0] * 4
        if lefty > 0:
            pre_sum = [pre[lefty-1] for pre in factor_list]
        post_sum = [post[Q[j]] for post in factor_list]
        for k in xrange(4):
            if post_sum[k] > pre_sum[k]:
                P[j] = k + 1
                break
    return P
