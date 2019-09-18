#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        n = len(s)
        if n % 2:
            return False
        mapping = {")": "(", "}": "{", "]": "["}
        s_stack = []
        for c in s:
            if c in mapping.keys():
                top_value = s_stack.pop() if s_stack else ""
                if top_value != mapping[c]:
                    return False
            else:
                s_stack.append(c)

        return not s_stack


if __name__ == '__main__':
    s1 = "([]{})[{}]"
    print(Solution().isValid(s1))
    s2 = "()[)"
    print(Solution().isValid(s2))
    s3 = "([)]"
    print(Solution().isValid(s3))
