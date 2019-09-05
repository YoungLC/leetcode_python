#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 方法1 暴力两层循环O（n2）
        # t = len(nums)
        # for i in range(t - 1):
        #     for j in range(i + 1, t):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # 方法2 HashMap 字典，两次循环
        # nums_map = {}
        # for i, v in enumerate(nums):
        #     nums_map[v] = i
        # for i, v in enumerate(nums):
        #     if nums_map.get(target - v, i) != i:
        #         return [i, nums_map.get(target - v)]
        #

        # 方法3 一次循环，在该元素的前端寻找
        nums_map = {}
        for i, v in enumerate(nums):
            s = nums_map.get(target - v)
            # 必须为Not None，不能是if s，s有可能为0
            if s is not None:
                return [s, i]
            nums_map[v] = i


if __name__ == '__main__':
    List = [2, 7, 11, 5]
    T = 9
    print(Solution().twoSum(List, T))
