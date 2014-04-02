#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(A):
    a_len = len(A) - 1
    left = A[0]
    right = sum(A) - A[0]
    minimal = abs(left - right)
    for i in range(1, a_len):
        left += A[i]
        right -= A[i]
        if minimal > abs(left - right):
            minimal = abs(left - right)
    return minimal

