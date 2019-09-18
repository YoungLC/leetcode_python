#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0
        max_num = nums[0]
        for i in range(0, len(nums)):
            total_sum += nums[i]
            if total_sum > max_num:
                max_num = total_sum
            if total_sum < 0:
                total_sum = 0
        return max_num


if __name__ == '__main__':
    # Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    # Output: 6
    # Explanation: [4, -1, 2, 1]
    t1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(t1))
