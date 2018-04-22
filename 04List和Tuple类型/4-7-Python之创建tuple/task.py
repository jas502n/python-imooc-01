#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
task.py
创建一个tuple，顺序包含0 - 9这10个数。
'''

# the first
t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print t

# second range函数方法：支持3个参数，start起始元素，stop结束元素，元素之间的间隔（默认为0）
T = tuple(x for x in range(0,10))
print T

s = range(10)
print '列表s为：', s
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 将list列表s转换成tuple元组
H = tuple(s)

print '将list列表s转换成tuple元组后为：', H