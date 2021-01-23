# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res=[]
        def dfs(x,res):
            if not x: return
            dfs(x.right,res)
            res.append(x.val)
            dfs(x.left,res)

        dfs(root,res)
        return res[k-1]





if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(1)
    c = TreeNode(4)
    d = TreeNode(2)
    a.left = b
    a.right = c
    b.right = d
    k = 1
    print(Solution().kthLargest(a, k))
