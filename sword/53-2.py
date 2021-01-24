# -*- coding: utf-8 -*-
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if nums[0] != 0:
            return 0
        if nums[n - 1] != n:
            return n
        for i in range(1, n):
            if nums[i] - nums[i - 1] != 1:
                return nums[i] - 1


if __name__ == '__main__':
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(Solution().missingNumber(a))
