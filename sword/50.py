# -*- coding: utf-8 -*-

class Solution(object):
    # def firstUniqChar(self, s):
    #     for c in s:
    #         if s.find(c) == s.rfind(c):
    #             return c
    #     return " "
    def firstUniqChar(self, s):
        res = {}
        for c in s:
            if res.get(c):
                res[c] += 1
            else:
                res[c] = 1
        for c in s:
            if res.get(c) == 1:
                return c
        return " "


if __name__ == '__main__':
    s = "cc"
    print(Solution().firstUniqChar(s))
