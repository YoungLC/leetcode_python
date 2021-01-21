class Solution(object):

    def mod(self,a, b):
        c = a // b
        r = a - c * b
        return r

    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1:
            return 1
        a,b=1,1
        for i in range(2,n+1):
            a,b=b,a+b

        return self.mod(b,1000000007)

