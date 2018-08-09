#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.

注意：

    输入的数组只包含 0 和1。
    输入数组的长度是正整数，且不超过 10,000。


"""


# 最大的0或1的个数

# class Solution(object):
#     def findMaxConsecutiveOnes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         zero_number = 1
#         ones_number = 1
#         max_zero = 1
#         max_one = 1
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1]:
#                 if nums[i]:
#                     ones_number += 1
#                 else:
#                     zero_number += 1
#             else:
#                 zero_number = 1
#                 ones_number = 1
#             max_zero = zero_number if zero_number > max_zero else max_zero
#             max_one = ones_number if ones_number > max_one else max_one
#         return max(max_zero, max_one)

# 最大的1的个数

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one_number = -1
        max_one = -1
        if nums.count(1):
            for i in range(1, len(nums)):
                if nums[i] and nums[i] == nums[i - 1]:
                    one_number += 1
                else:
                    one_number = 1
                max_one = one_number if one_number > max_one else max_one
            return max_one
        else:
            return 0


if __name__ == '__main__':
    test = [0]
    print Solution().findMaxConsecutiveOnes(test)
