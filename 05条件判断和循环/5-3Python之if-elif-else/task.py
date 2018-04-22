#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
task.py
当 age = 8 时，结果正确，但 age = 20 时，为什么没有打印出 adult

age = 8
if age >= 6:
    print 'teenager'
elif age >= 18:
    print 'adult'
else:
    print 'kid'
'''

# age = int(raw_input('请输入你的年龄：'))
age = 20
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
else:
    print 'kid'


# 如果按照分数划定结果：
#
#     90分或以上：excellent
#
#     80分或以上：good
#
#     60分或以上：passed
#
#     60分以下：failed

score = int(raw_input('请输入你的成绩：'))
if score >= 90:
    print 'excellent'
elif score >= 80:
    print 'good'
elif score >= 60:
    print 'passed'
else:
    print 'failed'
