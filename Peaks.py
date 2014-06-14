def solution(A):
    A_len = len(A)
    peaks_until_here = [0]*A_len
    for index in xrange(1, A_len-1):
        peaks_until_here[index] = peaks_until_here[index-1]
        if A[index] > A[index-1] and A[index] > A[index+1]:
            peaks_until_here[index] += 1
    if A_len < 3 or peaks_until_here[-2] == 0:
        return 0
    peaks_until_here[-1] = peaks_until_here[-2]
 
    max_blocks = 0
    for candidate in xrange(1, int(A_len ** 0.5)+1, 1):
        if A_len % candidate == 0:
            blocks, block_size = candidate, A_len // candidate
            for each_block in xrange(block_size - 1, A_len - block_size, block_size):
                if peaks_until_here[each_block] == \
                   peaks_until_here[each_block + block_size]:
                    break
            else:
                max_blocks = blocks
 
            if candidate * candidate == A_len:
                continue
 
            block_size, blocks = candidate, A_len // candidate
            for each_block in xrange(block_size - 1, A_len - block_size, block_size):
                if peaks_until_here[each_block] == \
                   peaks_until_here[each_block + block_size]:
                    break
            else:
                return blocks
 
    return max_blocks
