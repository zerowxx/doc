#!/usr/bin/env python
# -*- coding: utf-8 -*-
#读文件
try:
    f = open('module.py','r')
    print f.read()
finally:
    if f:
        f.close

with open('module.py', 'r') as f:
    print f.read()

#要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件
#codecs模块帮我们在读文件时自动转换编码，直接读出unicode

#写文件:写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件

#操作文件和目录:使用os模块

#序列化:从内存中变成可存储或传输的过程.Python提供两个模块来实现序列化：cPickle和pickle

#JSON:内置json模块



