def solution(A):
    A_len = len(A)
    A_max = max(A)
    counter = {}
    divisors = {}
    # counter counts occurences of numbers
    # divisor is just initialized by 1
    # (only known common divisor)
    for num in A:
        counter[num] = counter.get(num, 0) + 1
        divisors[num] = [1]
    
    # Divisors lower than sqrt(A_max)
    for divisor in xrange(2, int(A_max ** 0.5) + 1):
        multiple = divisor
        while multiple <= A_max:
            if multiple in divisors and not divisor in divisors[multiple]:
                divisors[multiple].append(divisor)
            multiple += divisor
    
    # Divisors higher than sqrt(A_max), no duplicates
    for num in divisors:
        temp = [num//div for div in divisors[num] \
            if num//div not in divisors[num]]
        divisors[num].extend(temp)
 
    result = []
    # For each number in A, we take his divisors
    # multiply by occurence, sum and substract from len(A)
    # because we want non-divisors count
    for num in A:
        result.append(A_len - sum([counter.get(
            div, 0) for div in divisors[num]]))
 
    return result
