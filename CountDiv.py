def solution(A, B, K):
    if A % K:
        return (B - (A - A % K)) // K    
    return ((B - A) // K) + 1
