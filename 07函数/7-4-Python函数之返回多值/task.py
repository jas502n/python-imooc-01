#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
一元二次方程的定义是：ax² + bx + c = 0
请编写一个函数，返回一元二次方程的两个解。
求根公式：https://baike.baidu.com/item/%E5%85%AC%E5%BC%8F%E6%B3%95/10260961?fr=aladdin
math.sqrt(9)
>>> 3.0

'''

import math

def quadratic_equation(a, b, c):
    x = b **2 -4*a*c
    if x >=0:
        x1 = (-b + math.sqrt(x)) / (2*a)
        x2 = (-b - math.sqrt(x)) / (2*a)
        return x1, x2
    else:
        return
print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)