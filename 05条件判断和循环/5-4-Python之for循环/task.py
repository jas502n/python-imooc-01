#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
task.py
班里考试后，老师要统计平均成绩，已知4位同学的成绩用list表示如下：
'''

L = [75, 92, 59, 68]
sum = 0.0
n = 0
for score in L:
    sum += score
    n = n +1
print '4位同学的平均成绩为%s分' % (sum / n)

