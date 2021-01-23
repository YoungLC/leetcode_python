# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        # def bfs():
        #     if not root:
        #         return []
        #     a=[]
        #     a.append(root)
        #     out_put=[]
        #     while a:
        #         tmp=[]
        #         for i in xrange(len(a)):
        #             node = a.pop(0)
        #             if node.left: a.append(node.left)
        #             if node.right: a.append(node.right)
        #             tmp.append(node.val)
        #         out_put.append(tmp)
        #     return out_put
        #
        # return bfs()
    # def levelOrder(self, root):
        def dfs(x, level, output):
            if not x:
                return []
            if level >= len(output):
                output.append([])
            output[level].append(x.val)
            dfs(x.left, level + 1, output)
            dfs(x.right, level + 1, output)

        output = []
        dfs(root, 0, output)
        return output


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    a.left = b
    a.right = c
    c.left = d
    print(Solution().levelOrder(a))
