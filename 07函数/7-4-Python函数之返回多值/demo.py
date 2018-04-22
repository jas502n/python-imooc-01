#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
demo.py
'''

import math
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print x, y
# 在语法上，返回一个tuple可以省略括号
