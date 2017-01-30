#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {
	'Michael':95, 
	'Bob':85,
	'Tom':90
	}
print('d[\'Michael\'] = %d' %d['Michael'])
print('d[\'Bob\'] = %d' %d['Bob'])
print('d[\'Jace\'] = %d' %d.get('Jace',-1))
