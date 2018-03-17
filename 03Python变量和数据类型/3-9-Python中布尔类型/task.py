#!/usr/bin/python
# -*- coding: utf-8 -*-


### 与运算： 只有两个布尔值都为 True 时，计算结果才为 True。 and
### 或运算： 只要有一个布尔值为 True，计算结果就是 True。 or


### 因为Python把0、空字符串''和None看成 False，其他数值和非空字符串都看成 True

### 1. 在计算 a and b 时，如果 a 是 False，则根据与运算法则，整个结果必定为 False，因此返回 a；如果 a 是 True，则整个计算结果必定取决与 b，因此返回 b。
### 2. 在计算 a or b 时，如果 a 是 True，则根据或运算法则，整个计算结果必定为 True，因此返回 a；如果 a 是 False，则整个计算结果必定取决于 b，因此返回 b。


a = 'python'   ### a为True ， 

print 'hello,', a or 'world' ###  true or 'world' 

### > hello python

b = ''   ### b为False

print 'hello,', b or 'world' ### Flase or True 

### >>>hello world


