# -*- coding: utf-8 -*-
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=0
        while n:
            if n&1 ==1:
                res+=1
            n>>=1

        return res



if __name__ == '__main__':
    print(Solution().hammingWeight(00000000000000000000000000001011))