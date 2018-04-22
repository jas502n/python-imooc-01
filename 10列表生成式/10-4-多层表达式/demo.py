#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
for循环可以嵌套，因此，在列表生成式中，也可以用多层 for 循环来生成列表。
对于字符串 'ABC' 和 '123'，可以使用两层循环，生成全排列：
'''

print [m + n for m in 'ABC' for n in '123']

sum = []
for m in 'ABC':
    for n in '123':
        sum.append(m + n)
print sum