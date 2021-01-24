# -*- coding: utf-8 -*-
import heapq


class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 系统函数
        # arr.sort()
        # return arr[0:k]
        if k ==0:
            return []
        res = [-x for x in arr[:k]]
        heapq.heapify(res)
        for i in range(k, len(arr)):
            if -res[0] > arr[i]:
                heapq.heappop(res)
                heapq.heappush(res, -arr[i])
        return [-x for x in res]

if __name__ == '__main__':
    a=[0, 0, 1, 2, 4, 2, 2, 3, 1, 4]
    b=8
    print(Solution().getLeastNumbers(a,b))