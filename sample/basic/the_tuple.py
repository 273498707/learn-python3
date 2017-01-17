#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ('Michael', 'Bob', 'Tracy')
#print('classmates= %s' %(classmates) )
print('classmates= ', classmates)
print('len(classmates) = %d' %(len(classmates)) )
print('classmates[0]= %s' %(classmates[0]) )
print('classmates[1]= %s' %(classmates[1]) )
print('classmates[2]= %s' %(classmates[2]) )
print('classmates[-1]= %s' %(classmates[-1]) )

tuples = ('a', 'b', ['A', 'B'])
print('tuples= ', tuples)
tuples[2][0] = 'X'
tuples[2][1] = 'Y'
print('tuples= ', tuples)
#cannot modify tuple:
#classmates[0] = 'Adam'
