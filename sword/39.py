class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        if len(nums) ==1:
            return nums[0]
        len_list = len(nums)
        hash_table = {}
        len_list = len(nums)
        for i in xrange(len_list):
            num = hash_table.get(nums[i])
            if not num:
                hash_table[nums[i]] = 1
            else:
                hash_table[nums[i]] += 1
            if num and num + 1 > len_list / 2:
                return nums[i]


if __name__ == '__main__':
    test = [1]
    print(Solution().majorityElement(test))
