#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(X, Y, D):
    dist = Y - X
    jumps, extra = divmod(dist, D)
    return jumps + (1 if extra else 0)

