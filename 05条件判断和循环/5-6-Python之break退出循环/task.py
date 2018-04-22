#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
task.py
利用 while True 无限循环配合 break 语句，计算 1 + 2 + 4 + 8 + 16 + ... 的前20项的和。
2 ** 0 + 2 **1 + 2**2 + .... + 2 ** 19
n (0,19)
'''

a1 = 1
sum = 0
n = 0
while True:
    x = 2 ** n
    print '第%s项的值为%s' % (n+1, x)
    sum += 2 ** n
    n += 1
    if n >= 20:
         break
print '\n前20项的和为%s' % sum

