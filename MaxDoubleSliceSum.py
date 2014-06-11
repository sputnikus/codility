def solution(A):
    A_len = len(A)
    # https://en.wikipedia.org/wiki/Maximum_subarray_problem
    max_ending_here = [0] * A_len
    max_so_far = 0
    for index in xrange(1, A_len - 1): # X + 1
        max_so_far = max(0, A[index] + max_so_far)
        max_ending_here[index] = max_so_far
    
    # https://en.wikipedia.org/wiki/Maximum_subarray_problem reversed
    max_beginning_here = [0] * A_len
    max_so_far = 0
    for index in xrange(A_len - 2, 0, -1): # Z - 1
        max_so_far = max(0, A[index] + max_so_far)
        max_beginning_here[index] = max_so_far
    
    # Y - 1 => Y + 1
    double_slice = 0
    for index in xrange(0, A_len-2):
        double_slice = max(double_slice,
            max_ending_here[index] + max_beginning_here[index+])
 
    return double_slice
