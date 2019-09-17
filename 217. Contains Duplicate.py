#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 方法1 时间O(n) 空间O(n)
        # v_map = {}
        # for i, v in enumerate(nums):
        #     if v_map.get(v, None) is not None:
        #         return True
        #     v_map[v] = i
        # return False
        #
        # 方法2 Set
        return len(nums) != len(set(nums))


if __name__ == '__main__':
    t1 = [1, 2, 3, 1]
    t2 = [1, 2, 3, 4]
    t3 = [1, 1]
    # print(Solution().containsDuplicate(t1))
    # print(Solution().containsDuplicate(t2))
    print(Solution().containsDuplicate(t3))
