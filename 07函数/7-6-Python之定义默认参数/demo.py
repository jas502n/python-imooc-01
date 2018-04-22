#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
demo.py
'''
# 例如Python自带的 int() 函数，其实就有两个参数，我们既可以传一个参数，又可以传两个参数：
# int()函数的第二个参数是转换进制，如果不传，默认是十进制 (base=10)，如果传了，就用传入的参数。

# 例如：将8进制转换成10进制

print int('123', 8)  # 83
print int('78', 16)  # 120

# 我们来定义一个计算 x 的N次方的函数:

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1    #由于是计算x 的N次方的函数，例如：2^3 ,s=1，n=3-1=2,s=1*2, 由于while循环，此时n=2,所以n=2-1=1,s=(1*2)*2;此时n还是>0,继续进入循环;n=1-1=0，s=((1*2)*2)* 2;此时n=0，退出循环，返回s
        s = s * x
    return s
print power(2, 3)

# 假设计算平方的次数最多，我们就可以把 n 的默认值设定为 2：
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print power(5)
