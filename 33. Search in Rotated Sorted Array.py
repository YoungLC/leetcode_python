#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0
            while left <= right:
                middle = (left + right) // 2
                if nums[middle] > nums[middle + 1]:
                    return middle + 1

                else:
                    if nums[middle] < nums[left]:
                        right = middle - 1
                    else:
                        left = middle + 1
            return

        def search(left, right):
            while left <= right:
                middle = (left + right) // 2
                if nums[middle] == target:
                    return middle
                else:
                    if nums[middle] > target:
                        right = middle - 1
                    else:
                        left = middle + 1
            return -1

        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1

        rotate_index = find_rotate_index(0, n - 1)
        if rotate_index == 0:
            return search(0, n - 1)
        if target < nums[0]:
            return search(rotate_index, n - 1)
        else:
            return search(0, rotate_index)


if __name__ == '__main__':
    # Example
    # 1:
    #
    # Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
    # Output: 4
    # Example
    # 2:
    #
    # Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
    # Output: -1
    nums = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0
    target2 = 3
    print(Solution().search(nums, target1))
    print(Solution().search(nums, target2))
