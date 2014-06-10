from collections import Counter

def solution(A):
    try:
        elem, num = Counter(A).most_common(1)[0]
    except IndexError:
        return -1
    if num > (len(A) // 2):
        return A.index(elem)
    return -1
