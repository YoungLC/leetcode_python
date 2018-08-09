#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

"""


# 这个数组有什么特点呢？首位字符肯定都是正数，只会在中间出现负数
# 算出总和，找出结果的最高点y,以及上升区间的第一个非负值


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
    test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    test = [-2,-1]
    # test = [1, 1, -2]
    # test = [-1, -2]
    # test = [-3, -2, 0, -1]
    # test = [-1, 0, -2]
    print Solution().maxSubArray(test)
