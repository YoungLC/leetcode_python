class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        large_num = 10**n-1
        return [i for i in range(1,large_num+1)]