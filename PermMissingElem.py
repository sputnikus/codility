#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(A):
    try:
        # 2 - one for range, one for missing
        return (set(range(1, len(A) + 2)) - set(A)).pop()
    except KeyError:
        return 1

