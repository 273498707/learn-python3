#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
n = -10
print(my_abs(n))