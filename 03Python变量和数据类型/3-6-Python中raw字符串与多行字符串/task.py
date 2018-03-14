#!/usr/bin/python
# -*- coding: utf-8 -*-


### task01
### 请把下面的字符串用r'''...'''的形式改写，并用print打印出来：
### '\"To be, or not to be\": that is the question.\nWhether it\'s nobler in the mind to suffer.'

s = r'''\"To be, or not to be\": that is the question.\nWhether it\'s nobler in the mind to suffer.'''
### r: 表示这是一个 raw 字符串，里面的字符就不需要转义了
print s 

d = '"To be, or not to be\": that is the question.\nWhether it\'s nobler in the mind to suffer.'
### 转义
### \n 换行
### \t 表示一个制表符
### \\ 表示 \ 字符本身
print d 

