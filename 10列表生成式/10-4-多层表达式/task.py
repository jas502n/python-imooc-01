#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
任务
利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。
'''
# 第一种方法
sum = []
for x in range(1,10):
    for y in range(0,10):
        for z in range(1,10):
            if x == z :
                sum.append(int(str(x)+str(y)+str(z)))
print sum

# 第二种方法
print [int(str(x)+str(y)+str(z)) for x in range(1,10) for y in range(0,10) for z in range(1,10) if x == z]

# 第三种方法
print [100*m+10*n+m for m in range(1,10) for n in range (0,10)]

L = []
for x in range(1,10):
    for y in range(0,10):
        L.append(100 * x + 10 * y +x)
print L

# 第四种方法
print [x for x in range(100,1000) if  x / 100 == x % 10]

# 第五种方法
x = []
for i in range(100,1000):
    if str(i)[::-1] == str(i):
        x.append(i)
print x

print [i for i in range(100,1000) if str(i)[::-1] == str(i) ]



