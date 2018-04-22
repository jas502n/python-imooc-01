#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
demo.py
'''

print [x * x for x in range(1, 11)]
# 写出for in 形式
sum = []
for i in range(1,11):
    sum.append(i * i)
print sum


# 列表生成式的 for 循环后面还可以加上 if 判断。例如：
#  如果我们只想要偶数的平方，不改动 range()的情况下，可以加上 if 来筛选：

print [x * x for x in range(1, 11) if x % 2 == 0]
# for in 迭代方式 + if 判断语句
sum = []
for x in range(1, 11):
    if x % 2 == 0:
        sum.append(x * x)
print  sum
