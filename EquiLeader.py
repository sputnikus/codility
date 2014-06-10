from collections import Counter

def solution(A):
    A_len = len(A)
    try:
        elem, occur = Counter(A).most_common(1).pop()
    except IndexError:
        return 0
    if occur <= (A_len // 2):
        return 0
    equi = 0
    equi_count = 0
    for i, value in enumerate(A):
        if value == elem:
            equi_count += 1
        if equi_count > (i + 1) // 2 and \
           (occur - equi_count) > (A_len - i - 1) // 2:
            equi += 1
 
    return equi
