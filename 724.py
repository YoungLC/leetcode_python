# class Solution(object):
#     def pivotIndex(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return -1
#         len_n = len(nums)
#         for i in range(len_n):
#             left, right = sum(nums[0:i]), sum(nums[i + 1:])
#             if left == right:
#                 return i
#         return -1


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        len_n = len(nums)
        total = sum(nums)
        left = 0
        for i in range(len_n):
            left = left + nums[i - 1] if i > 0 else left + 0
            right = total - nums[i] - left
            if left == right:
                return i
        return -1


if __name__ == '__main__':
    n = [-1, -1, -1, 0, 1, 1]
    print(Solution().pivotIndex(n))
