#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
weekdays.py
'''

weekdays = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])

x = raw_input('请输入星期几：')
if x in weekdays:
    print 'input ok'
else:
    print 'input error'