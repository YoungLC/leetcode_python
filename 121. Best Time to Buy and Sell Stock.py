#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 方法1
        # max_profit = 0
        # l_p = len(prices)
        # for i in range(l_p - 1):
        #     for j in range(i, l_p):
        #         profit = prices[j] - prices[i]
        #         if profit > max_profit:
        #             max_profit = profit
        #
        # return max_profit

        # 方法2
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        l_p = len(prices)
        for i in range(1, l_p):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit


if __name__ == '__main__':
    t1 = [7, 5, 3, 10, 4, 1, 9]
    # output1=5x
    t2 = [10, 2, 9, 1, 2, 1, 3, 1]
    # output2=0
    print(Solution().maxProfit(t1))
    print(Solution().maxProfit(t2))
