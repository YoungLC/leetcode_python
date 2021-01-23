# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # def dfs(x):
        #     if not x:
        #         return 0
        #     return max((1 + dfs(x.left)), (1 + dfs(x.right)))
        #
        # return dfs(root)
        if not root:
            return 0
        Q = []
        Q.append(root)
        depth = 1
        while Q:
            len_q = len(Q)
            for i in range(len_q):
                node = Q.pop(0)
                if node.left: Q.append(node.left)
                if node.right: Q.append(node.right)
                if not Q:
                    return depth
            depth += 1

        return depth




if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    c.right = e
    print(Solution().maxDepth(a))
