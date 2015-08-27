#!/usr/bin/env python
# -*- coding: utf-8 -*-

#multiprocessing模块:跨平台多进程
#from multiprocessing import Process
#import os
#
#def runProc(name):
#    print 'Run child process %s (%s)...' % (name, os.getpid())
#
#if __name__=='__main__':
#    print 'Parent process %s.' % os.getpid()
#    p = Process(target=runProc, args=('test',))
#    print 'Process will start.'
#    p.start()
#    p.join()
#    print 'Process end.'

#Pool
#from multiprocessing import Pool
#import os, time, random
#
#def long_time_task(name):
#    print 'Run task %s (%s)...' %(name, os.getpid())
#    start = time.time()
#    time.sleep(random.random()*5)
#    end = time.time
#    print 'Task %s runs %0.2f seconds.' % (name, (end-start))
#
#if __name__=='__main__':
#    print 'Parent process %s.' % os.getpid()
#    p = Pool()
#    for i in range(5):
#        p.apply_async(long_time_task, args=(i,))
#    print 'Wait for all subprocesses done...'
#    p.close()
#    p.join()
#    print 'All subproceses done.'

#进程间通讯
#from multiprocessing import Process, Queue
#import os, time, random
#
#def write(q):
#    for value in ['A', 'B', 'C']:
#        print 'Put %s to queue...' % value
#        q.put(value)
#        time.sleep(random.random())
#
#def read(q):
#    while True:
#        value = q.get(True)
#        print 'Get %s to queue...' % value
#
#if __name__ == '__main__':
#    q = Queue()
#    pw = Process(target=write, args=(q,))
#    pr = Process(target=read, args=(q,))
#    pw.start()
#    pr.start()
#    pw.join()
#    pr.terminate()

#多线程
#python提供thread和threading两个模块，thread是低级模块，threading是高级模块，封装了thread.
#import time, threading
#
#def loop():
#    print 'thread %s is runing..' % threading.current_thread().name
#    n = 0
#    while n < 5:
#        n = n + 1
#        print 'thread %s >>> %s' % (threading.current_thread().name, n)
#        time.sleep(1)
#    print 'thread %s ended.' % threading.current_thread().name
#
#print 'thread %s is running...' % threading.current_thread().name
#t = threading.Thread(target=loop, name='LoopThread')
#t.start()
#t.join()
#print 'thread %s ended.' % threading.current_thread().name

#Lock
#import time, threading
#
#balance = 0
#lock = threading.Lock()
#
#def change(n):
#    global balance
#    balance = balance + n
#    balance = balance - n
#
#def runThread(n):
#    for i in range(100000):
#        lock.acquire()
#        try:
#            change(n)
#        finally:
#            lock.release()
#
#t1 = threading.Thread(target=runThread, args=(5,))
#t2 = threading.Thread(target=runThread, args=(8,))
#t1.start()
#t2.start()
#t1.join()
#t2.join()
#print balance
    
#ThreadLocal
import threading
local_school = threading.local()

def process_student():
    print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)

def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

