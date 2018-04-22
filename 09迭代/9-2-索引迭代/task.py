#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
任务
zip()函数可以把两个 list 变成一个 list：
zip([10, 20, 30], ['A', 'B', 'C'])
[(10, 'A'), (20, 'B'), (30, 'C')]
在迭代 ['Adam', 'Lisa', 'Bart', 'Paul'] 时，如果我们想打印出名次 - 名字（名次从1开始)，请考虑如何在迭代中打印出来。
提示：考虑使用zip()函数和range()函数
'''

# s = ['Adam', 'Lisa', 'Bart', 'Paul']
# for index, name in enumerate(s):
#     print index + 1, '-', name

# L = ['Adam', 'Lisa', 'Bart', 'Paul']
# for index, name in zip(range(1, len(L)+1), L):
#     print index, '-', name


L = ['Adam', 'Lisa', 'Bart', 'Paul']
X = list(i for i in range(1,len(L)+1))
Y = zip(X, L)
print Y
for index, name in Y:
    print index, '-', name