class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        for i in range(l):
            if sum(nums[0:i]) == sum(nums[i+1:l]):
                return i
        return -1


if __name__ == '__main__':
    nums = [2, 1, -1]
    print(Solution().pivotIndex(nums))