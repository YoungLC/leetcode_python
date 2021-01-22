class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp_dict = {}
        n = len(nums)
        for i in range(n):
            if not tmp_dict.get(str(nums[i]), None):
                tmp_dict[str(nums[i])] = 1
            else:
                return nums[i]


if __name__ == '__main__':
    A = [2, 3, 1, 0, 2, 5, 3]
    print Solution().findRepeatNumber(A)
