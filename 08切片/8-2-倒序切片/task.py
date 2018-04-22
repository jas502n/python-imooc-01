#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
利用倒序切片对 1 - 100 的数列取出：

* 最后10个数；
* 最后10个5的倍数。
'''

L = range(1, 101)
print L[-10:]

s= L[4::5]
print s[-10:]
print L[4::5][-10:]

# 多维
print L[-10:]+L[4:5]

