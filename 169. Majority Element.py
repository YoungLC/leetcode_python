class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_list = list(set(nums))
        for item in set_list:
            if nums.count(item) > len(nums) / 2:
                return item
