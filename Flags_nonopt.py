def solution(A):
    A_len = len(A)
    next_peak = [-1] * A_len
    peaks_count = 0
    first_peak = -1
    
    for index in xrange(A_len - 2, 0, -1):
        if A[index] > A[index + 1] and A[index] > A[index - 1]:
            next_peak[index] = index
            peaks_count += 1
            first_peak = index
        else:
            next_peak[index] = next_peak[index + 1]
    if peaks_count < 2:
        return peaks_count
 
    max_flags = 1
    for min_distance in xrange(int(A_len ** 0.5), 1, -1):
        flags_used = 1
        flags_have = min_distance - 1
        pos = first_peak
        while flags_have > 0:
            if pos + min_distance >= A_len - 1:
                break
            pos = next_peak[pos + min_distance]
            if pos == -1:
                break
            flags_used += 1
            flags_have -= 1
        max_flags = max(max_flags, flags_used)
 
    return max_flags
