#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
task.py
对100以内的两位数，请使用一个两重循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）。
x < y
'''

for x in range(1,10):
    for y in range(1,10):
        if x >= y:
            continue
        print str(x)+str(y)   # 字符串拼接


