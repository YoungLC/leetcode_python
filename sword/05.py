# -*- coding: utf-8 -*-
class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp = ""
        for i in range(len(s)):
            if s[i].isspace():
                tmp = tmp + "%20"
            else:
                tmp = tmp + s[i]
        return tmp
