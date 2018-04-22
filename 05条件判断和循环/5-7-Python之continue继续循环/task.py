#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
task.py
对已有的计算 0 - 100 的while循环进行改造，通过增加 continue 语句，使得只计算奇数的和：
sum = 0
x = 1
while True:
    sum = sum + x
    x = x + 1
    if x > 100:
        break
print sum
'''

sum = 0.0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if not x % 2 :     # 当x= 奇数时，3 % 2 = true , not 3%2 = not(非空字符串true)，为false;
        continue       # 当x = 偶数时，4 %2 =0 ，python规定0 是flase ，not 4 % 2 = true。
    print x            # 如果 if 语句判断为 True，就会执行这个代码块，所以这代码过滤的是偶数
    sum = sum + x
print sum



