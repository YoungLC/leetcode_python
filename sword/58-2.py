# -*- coding: utf-8 -*-
class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        len_s=len(s)
        l,r=[],[]
        for i in range(len_s):
            if i<n:
                l.append(s[i])
            else:
                r.append(s[i])
        r.extend(l)
        return "".join(r)





if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    print(Solution().reverseLeftWords(s,k))