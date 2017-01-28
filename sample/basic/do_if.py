#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import platform

print(platform.python_version())

# notes:
# input() returns strings
# int(string) return a Integer
age = int(input('Input your age: '))

if age >= 18:
    print('adult')
elif age >= 6:
	print('teenager')
else:
	print('kild')

