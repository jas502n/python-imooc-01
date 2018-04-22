#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
sum()函数接受一个list作为参数，并返回list所有元素之和。
'''

# 第一种方法：
sum = 0
for i in range(1, 101):
    sum += i * i
print sum

# 第二种方法：
print sum([i*i for i in range(1,101)])

