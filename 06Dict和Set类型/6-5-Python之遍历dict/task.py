#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
task.py
请用 for 循环遍历如下的dict，打印出 name: score 来。
'''

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}

for k in d:
    print k + ': ' + str(d.get(k))