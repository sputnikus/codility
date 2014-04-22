#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(N, A):
    counters = [0] * N
    last_max = max_count = 0
    for ind in A:
        if ind > N:
            last_max = max_count
            continue
        if counters[ind-1] < last_max:
            counters[ind-1] = last_max
        counters[ind-1] += 1
        if counters[ind-1] > max_count:
            max_count = counters[ind-1]
    for i in xrange(N):
        if counters[i] < last_max:
            counters[i] = last_max
    return counters

