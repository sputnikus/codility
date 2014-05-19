def solution(A):
    len_a = len(A)
    min_avg_slice = (A[0] + A[1]) / 2.0
    min_start_pos = 0
    for i in range(len_a - 1):
        local_two_sum = (A[i] + A[i + 1])
        if (local_two_sum / 2.0) < min_avg_slice:
            min_avg_slice = (local_two_sum / 2.0)
            min_start_pos = i
            continue
        try:
            local_three_sum = local_two_sum + A[i + 2]
            if (local_three_sum / 3.0) < min_avg_slice:
                min_avg_slice = (local_three_sum / 3.0)
                min_start_pos = i
        except IndexError:
            break
    return min_start_pos
