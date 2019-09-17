#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        n = len(nums)
        for k in range(n - 2):
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            l, r = k + 1, n - 1
            while l < r:
                sum = nums[k] + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif sum < 0:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    res.append([nums[k], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res


if __name__ == '__main__':
    # nums = [-1, 0, 1, 2, -1, -4],
    #
    # A
    # solution
    # set is:
    # [
    #     [-1, 0, 1],
    #     [-1, -1, 2]
    # ]
    nums = [-1, 0, 1, 2, -1, -4]
    # nums = [2, 4, 1, 0, -3, -1]
    print(Solution().threeSum(nums))
