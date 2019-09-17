#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # # 时间复杂度 O(n),空间复杂度 O(n),但题目要求不能有除法
        # output = []
        # sum = 1
        # zero_num = 0
        # for i, v in enumerate(nums):
        #     if v:
        #         sum *= v
        #     else:
        #         zero_num += 1
        #
        # if zero_num > 1:
        #     return [0] * len(nums)
        #
        # for i, v in enumerate(nums):
        #     if zero_num == 1:
        #         if v:
        #             output.append(0)
        #         else:
        #             output.append(sum)
        #     else:
        #         output.append(sum / v)
        #
        # return output

        l_nums = len(nums)
        res = [1] * l_nums
        for i in range(1, l_nums):
            res[i] = res[i - 1] * nums[i - 1]
        x = 1
        for i in range(l_nums - 1, -1, -1):
            res[i] = res[i] * x
            x *= nums[i]
        return res


if __name__ == '__main__':
    # Input:  [1, 2, 3, 4]
    # Output: [24, 12, 8, 6]
    t1 = [1, 2, 3, 4]
    print(Solution().productExceptSelf(t1))
