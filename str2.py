class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        for i in range(l):
            if nums[i] >= target:
                return i
        return l



if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 7
    print(Solution().searchInsert(nums, target))
