#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
demo.py
'''

print  range(1, 11)

L = []
for x in range(1, 11):
    L.append(x * x)
print L

print [x * x for x in range(1, 11)]

# 列表生成式