#!/usr/bin/env python
# -*- coding: utf-8 -*-

#collections
#namedtuple:自定义tuple对象
from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print 'x:%s, y:%s' % (p.x, p.y)
Circle = namedtuple('Circle', ['x', 'y', 'r'])
#deque:高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('d')
q.appendleft('0')
print q
#defaultdict:key不存在返回默认值的dict'
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['a'] = '1'
print dd['key1'], dd['a']
#OrderedDict:Key会按照插入的顺序排列
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print d
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print od
#Counter:计数器。统计字符出现个数
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print c


#Base64:一种通过查表的编码方法，不能用于加密;适用于小段内容的编码，比如数字证书签名、Cookie的内容等
import base64
print base64.b64encode('binary\x00string')
print base64.b64decode('YmluYXJ5AHN0cmluZw==')

#struct:解决str和其他二进制数据类型的转换

#hashlib:提供了常见的摘要算法，如MD5，SHA1
import hashlib
md5 = hashlib.md5()
md5.update('111111')
print md5.hexdigest()

sha1 = hashlib.sha1()
sha1.update('111111')
print sha1.hexdigest()

#itertools:迭代工具
import itertools
ns = itertools.repeat('1', 10) #重复几次
for n in ns:
    print n
naturals = itertools.count(1) #自然数序列
cs = itertools.cycle('ABC') #重复
ns = itertools.takewhile(lambda x : x <= 10, naturals) #根据条件截取有限序列
for c in chain('ABC', 'XYZ') #串联ABC XYZ
#重复元素归类
for key, group in itertools.groupby('AABBDDEE'):
    print key, list(group)
#imap() ifilter()


#XML
#操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。

#HTMLParser

