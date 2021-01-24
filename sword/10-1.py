# -*- coding: utf-8 -*-
class Solution(object):

    def mod(self, a, b):
        c = a // b
        r = a - c * b
        return r

    def fib(self, n):

        if n == 0:
            return 0
        if n == 1:
            return 1

        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b

        return self.mod(b, 1000000007)


if __name__ == '__main__':
    print Solution().fib(100)
