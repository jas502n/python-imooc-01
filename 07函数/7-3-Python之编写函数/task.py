#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
请定义一个 square_of_sum 函数，它接受一个list，返回list中每个元素平方的和。
'''

def square_of_sum(L):
    # return ([i * i for i in L])
    sum = 0
    for i in L:
        sum += i * i
    return sum
print square_of_sum([1, 2, 3, 4, 5])
print square_of_sum([-5, 0, 5, 15, 25])

# print ([i*i for i in [1, 2, 3, 4, 5]])