class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(1, n+1):
            if "1" in str(i):
                res += str(i).count("1")
        return res


if __name__ == '__main__':
    n = 824883294
    print(Solution().countDigitOne(n))
