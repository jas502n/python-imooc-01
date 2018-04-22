#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
task.py
利用while循环计算100以内奇数的和。
'''


x = 1
sum = 0
while x < 100:
    print x
    sum += x
    x += 2
print '100以内奇数的和为%s' % sum

