#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def my_abs(x):
	result = x
	if x > 0: result = x
	elif x == 0: result = 0
	else: result = -x
	return result
n = -10
print(my_abs(n))