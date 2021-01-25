class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # ji = []
        # ou = []
        # for i in xrange(len(nums)):
        #     if nums[i] % 2 == 0:
        #         ou.append(nums[i])
        #     else:
        #         ji.append(nums[i])
        # ji.extend(ou)
        # return ji
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            if nums[l] % 2 == 1:
                l += 1
            elif nums[r] % 2 == 0:
                r -= 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        return nums