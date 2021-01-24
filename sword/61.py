# -*- coding: utf-8 -*-
class Solution(object):

    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        h = {}
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            if not h.get(nums[i]):
                h[nums[i]] = 1
            else:
                return False
        if max(h.keys()) - min(h.keys()) <= 4:
            return True
        return False


if __name__ == '__main__':
    a = [11, 0, 9, 0, 0]
    print(Solution().isStraight(a))
