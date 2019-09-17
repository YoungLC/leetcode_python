#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

 

Example 1:

Input: [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
Example 2:

Input: [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.
 
'''
import thread
import time
from threading import RLock


def printFirst():
    print("first")


def printSecond():
    print("second")


def printThird():
    print("third")


method_map = {}


class Foo(object):
    def __init__(self):
        self.alock = RLock()
        self.block = RLock()

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        # printFirst() outputs "first". Do not change or remove this line.
        self.alock.acquire()
        printFirst()
        self.alock.release()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        # printSecond() outputs "second". Do not change or remove this line.
        self.block.acquire()
        if self.alock.acquire():
            printSecond()
            self.alock.release()
            self.block.release()
        else:
            time.sleep(0.01)

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        # printThird() outputs "third". Do not change or remove this line.
        if self.block.acquire():
            printThird()
            self.block.release()
        else:
            time.sleep(0.01)


def star_new_thread(input):
    a = Foo()
    thread_map = {
        "1": (a.first, printFirst),
        "2": (a.second, printSecond),
        "3": (a.third, printThird),
    }
    for i in input:
        thread.start_new_thread(thread_map[str(i)][0], (thread_map[str(i)][1],))
        time.sleep(1 * 0.01)


if __name__ == '__main__':
    test = [1, 3, 2]
    star_new_thread(test)
