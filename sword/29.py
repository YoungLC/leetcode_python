# -*- coding: utf-8 -*-
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        res = []
        while len(matrix) > 0 and len(matrix[0]) > 0:
            x = len(matrix)
            y = len(matrix[0])
            if x == 1:
                res.extend(matrix[0])
                break
            if y == 1:
                res.extend([matrix[i][0] for i in range(x)])
                break
            res.extend(matrix[0])
            res.extend([matrix[i][y - 1] for i in range(1, x - 1)])
            res.extend(matrix[-1][::-1])
            res.extend([matrix[i][0] for i in range(x - 2, 0, -1)])
            matrix = [[matrix[i][j] for j in range(1, y - 1)] for i in range(1, x - 1)]
        return res


if __name__ == '__main__':
    x = matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(Solution().spiralOrder(x))
