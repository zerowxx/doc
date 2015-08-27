#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.__age = age
        self.score = score

    def getAge(self):
        return self.__age

    def setAge(self, age):
        if 0<= age <= 150:
            self.__age = age
        else:
            raise ValueError('wrong age!')
    
    def getScore(self):
        print '%s: %s' % (self.name, self.score)

    def getGrade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return 'C'

bart = Student('Zero', 1, 100)
bart.getScore()
print '%s: %s' % (bart.name, bart.getGrade())

#private变量设置访问
bart.setAge(25)
print '%s: %s' % (bart.name, bart.getAge())


#继承与多态
class Animal(object):
    def run(self):
        print 'Animal is running...'

class Dog(Animal):
    def run(self):
        print 'Dog is running...'

class Cat(Animal):
    def eat(self):
        print 'Cat eat fish...'

animal = Animal()
dog = Dog()
cat = Cat()
animal.run()
dog.run()
cat.run()
cat.eat()

#获取对象信息
#type():判断对象类型
#isinstance():继承关系判断对象是否是某种类型
#dir():获取一个对象所有属性和方法

#动态绑定
class Student(object):
    pass
#给实例绑定属性
s = Student()
s.name = 'aaaa'
print s.name
#给实例绑定方法
def setAge(self, age):
    self.age = age

from types import MethodType
s.setAge = MethodType(setAge, s, Student)
s.setAge(25)
print s.age
#给类绑定方法
def setScore(self, score):
    self.score = score
Student.setScore = MethodType(setScore, None, Student)
s.setScore(99)
print s.score

#使用__slots__限制类属性,但对子类无效
class A(object):
    __slots__ = ('name', 'age')#只允许绑定name和age属性

#使用@property装饰器把方法变成属性调用
class StudentA(object):
    
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be Integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self._score = value
sa = StudentA()
sa.score = 66
print sa.score

#多重继承

#定制类
class StudentB(object):
    def __init__(self, name):
        self.__name = name
    #返回用户看到的字符串
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    #返回程序开发者看到的字符串,调试用
    __repr__ = __str__

#__iter__
class Fib(object):
    def __init__(self):
        self.a,self.b = 0, 1
    def __iter__(self):
        return self
    def next(self):
        self.a, self.b = self.b, self.a+self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a
for n in Fib():
    print n
#__getitem__
#__getattr__
#__call__


#元类***

