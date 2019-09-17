#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l_nums = len(nums)
        products = 1
        max_sum = -sys.maxint
        for i in range(l_nums):
            products *= nums[i]
            if max_sum < products:
                max_sum = products
            if products == 0:
                products = 1
        products = 1
        for i in range(l_nums):
            products *= nums[l_nums - i - 1]
            if max_sum < products:
                max_sum = products
            if products == 0:
                products = 1
        return max_sum


if __name__ == '__main__':
    """
    Example 1:
    Input: [2,3,-2,4]
    Output: 6


    Example 2:
    Input: [-2,0,-1]
    Output: 0
    """

    t1 = [2, 3, -2, 4]
    t2 = [-2, 0, -1]
    t3 = [-4, -3]
    t4 = [0, 2]
    t5 = [3, -1, 4]
    print(Solution().maxProduct(t1))
    print(Solution().maxProduct(t2))
    print(Solution().maxProduct(t3))
    print(Solution().maxProduct(t4))
    print(Solution().maxProduct(t5))
