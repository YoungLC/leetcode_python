#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l_nums = len(nums)
        if l_nums == 1:
            return nums[0]
        flag_num = nums[0]
        for i in range(1, l_nums):
            if nums[i] > flag_num:
                flag_num = nums[i]
            else:
                return nums[i]
        return nums[0]


if __name__ == '__main__':
    # Example
    # 1:
    #
    # Input: [3, 4, 5, 1, 2]
    # Output: 1
    # Example
    # 2:
    #
    # Input: [4, 5, 6, 7, 0, 1, 2]
    # Output: 0
    t1 = [3, 4, 5, 1, 2]
    t2 = [4, 5, 6, 7, 0, 1, 2]
    t3 = [1]
    t4 = [1, 2]
    print(Solution().findMin(t1))
    print(Solution().findMin(t2))
    print(Solution().findMin(t3))
    print(Solution().findMin(t4))
