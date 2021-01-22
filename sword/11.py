# -*- coding: utf-8 -*-
class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        if not numbers:
            return 0
        tmp = numbers[0]
        for i in range(1, len(numbers)):
            if numbers[i] < tmp:
                return numbers[i]

        return tmp
