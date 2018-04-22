#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
任务
请根据dict：
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
打印出 name : score，最后再打印出平均分 average : score。
iteritems() 不占用额外的内存
'''

# 第一种方法
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for k, v in d.items():
    sum = sum + v
    print k,':', v
print 'average', ':', sum/len(d.items())

# 第二种
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
for k, v in d.iteritems():
    print "%s : %d" % (k, v)
print "average",":" ,sum(d.itervalues())  / float(len(d))