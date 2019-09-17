#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        len_n = len(nums)
        for i in range(0, len_n - 1):
            for j in range(i + 1, len_n):
                if not nums[i] and nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp


if __name__ == '__main__':
    test = [0, 1, 0, 3, 12]
    Solution().moveZeroes(test)
    print test
