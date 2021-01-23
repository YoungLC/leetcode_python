# -*- coding: utf-8 -*-
class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        # """暴力"""
        # # res=[]
        # # for i in xrange(1,target):
        # #     for j in xrange(i,target):
        # #         tmp_list= [m for m in xrange(i,j+1)]
        # #         if sum(tmp_list) == target:
        # #             res.append(tmp_list)
        # #
        # # return res
        #
        res=[]
        l,r = 1,2
        while l<r and r< target:
            sum_of_num=(l+r)*(r-l+1)/2
            if int(sum_of_num) == target:
                # print((l,r,sum_of_num))
                res.append([i for i in xrange(l,r+1)])
                l+=1
            elif int(sum_of_num) <target:
                r+=1
            else:
                l+=1
        return res












if __name__ == '__main__':
    print(Solution().findContinuousSequence(9))

