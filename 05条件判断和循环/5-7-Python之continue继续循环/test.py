#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
test.py
'''
print '打印continue循环:'
L = [75, 98, 59, 81, 66, 43, 69, 85]
s = 0.0
n = 1
for a in L:
    if a < 60:
        continue  #跳出当次循环，中断循环，继续执行下一个
    s = s + a
    print a
    n = n + 1

print '\n打印for循环:'
for x in range(1,10,1):
    if x == 5:   # print x语句只打到4的时候就终止了
        break
    print x