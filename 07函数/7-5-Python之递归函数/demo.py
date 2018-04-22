#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
fact(n) = n! = 1 * 2 * 3 * ... * (n-1) * n = (n-1)! * n = fact(n-1) * n
所以，fact(n)可以表示为 n * fact(n-1)，只有n=1时需要特殊处理。

'''

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print fact(3)
print fact(5)
print fact(100)

# print fact(1000)=1000 * 999 * 998 * 1
# most recent call last

# 使用递归函数需要注意防止栈溢出。
# 在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
# 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
# 由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试计算 fact(10000)。