# -*- coding: utf-8 -*-
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 暴力法，超时
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i,n):
        #         if nums[i] + nums[j] ==target:
        #             return [nums[i],nums[j]]

        # 双指针,头尾法

        n = len(nums)
        if n <= 1:
            return []
        left, right = 0, n - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [nums[left], nums[right]]
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))
