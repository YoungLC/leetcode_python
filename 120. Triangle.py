class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        total_sum = 0
        def dfs(i, j, total_sum):
            if i == m:
                if total_sum < best:
                    best= total_sum
                return
            dfs(i + 1, j, total_sum + triangle[i][j])
            dfs(i + 1, j + 1, total_sum + triangle[i][j])

        dfs(0, 0, total_sum)

        return AA
