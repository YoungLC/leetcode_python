#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ns = len(s)
        nt = len(t)
        if ns != nt:
            return False
        s_map = {}
        for i in range(ns):
            if not s_map.get(s[i]):
                s_map[s[i]] = 1
            else:
                s_map[s[i]] += 1
        for j in range(nt):
            if s_map.get(t[j]) is None:
                return False
            else:
                if s_map[t[j]] > 0:
                    s_map[t[j]] -= 1
                else:
                    return False
        return True


if __name__ == '__main__':
    # Input: s = "anagram", t = "nagaram"
    # Output: true
    # Input: s = "rat", t = "car"
    # Output: false
    # s1, t1 = "anagram", "nagaram"
    # s2, t2 = "rat", "car"
    # print Solution().isAnagram(s1, t1)
    # print Solution().isAnagram(s2, t2)
    s3, t3 = "aacc", "ccac"

    print Solution().isAnagram(s3, t3)
