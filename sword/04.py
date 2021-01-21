class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        # m,i hang,   n,j lie
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i = i + 1
            elif matrix[i][j] > target:
                j = j - 1
        return False
