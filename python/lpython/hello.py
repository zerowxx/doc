#!/usr/bin/env python
# -*- coding: utf-8 -*-

#hello.py

print 'hello, world'

print u'中文'

##list 可变长度
classmates = ['Michael', 'Bob', 'Tracy']
print classmates
print 'len:',len(classmates)

#delete last
classmates.pop()
#classmates.pop(i)
print classmates

#insert
classmates.append('Tracy')
classmates.insert(1,'Jack')
print classmates

##tuple 固定不可变
a=(1,2,3)
print a

#小结:list和tuple是Python内置的有序集合，一个可变，一个不可变。

birth =int(raw_input('birth:'))
if birth<2000:
    print '00前'
else:
    print '00后'

#循环
for name in classmates:
    print name 

sum = 0
for x in [1,2,3,4,5]:
    sum = sum + x
print sum

for x in range(10):
    print x

#字典 key为不可变对象！
d = {'a':1,'b':2}
print d['a']

#和list比较，dict有以下几个特点：
#查找和插入的速度极快，不会随着key的增加而增加；
#需要占用大量的内存，内存浪费多。
#而list相反：
#查找和插入的时间随着元素的增加而增加；
#占用空间小，浪费内存很少。

#set 非重复元素
s = set([1,2,3])
print s
s.add(4)
print s
s.remove(1)
print s

#定义函数：def关键字 函数名 括号后加:
def myabs(x):
    if x >= 0:
        return x
    else:
        return -x

print myabs(-9)

#函数可以同时返回多个值，但其实就是一个tuple


