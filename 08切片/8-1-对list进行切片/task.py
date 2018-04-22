#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
range(1, 101)
[1, 2, 3, ..., 100]
请利用切片，取出：

1. 前10个数；
2. 3的倍数；
3. 不大于50的5的倍数。
'''

L = range(1, 101)


print L[0:10:1]  # 0-9 ,默认step=1
print L[2::3]    #3 (4,5) 6
print L[4:50:5]






