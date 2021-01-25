# -*- coding: utf-8 -*-
class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """

        def get_index_toal(n):
            if 0 <= n < 10:
                return n
            elif 10 <= n < 100:
                return n / 10 + n % 10
            else:
                return n / 100 + n / 10 + n % 10

        def get_toatal(i, j):
            return get_index_toal(i) + get_index_toal(j)

        def dfs(i, j, k, a):
            print(i, j)
            if not 0 <= i < m or not 0 <= j < n or get_toatal(i, j) > k or (i, j) in a:
                return 0
            a.add((i, j))
            return 1 + dfs(i + 1, j, k, a) + dfs(i, j + 1, k, a)

        a = set()

        return dfs(0, 0, k, a)


if __name__ == '__main__':
    m = 36
    n = 11
    k = 15
    print(Solution().movingCount(m, n, k))
