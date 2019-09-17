#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """




if __name__ == '__main__':
    # Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    # Output: 6
    # Explanation: [4, -1, 2, 1]
    t1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(t1))
