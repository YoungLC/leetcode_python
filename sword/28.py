# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def recur(L, R):
            if not L and not R:
                return True
            if not L or not R or L.val != R.val:
                return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        if not root:
            return True
        return recur(root.left, root.right)

        # if not root:
        #     return False
        # s, inorder = [], []
        # node = root
        # while len(s) > 0 or node is not None:
        #     if node is not None:
        #         s.append(node)
        #         node = node.left
        #     else:
        #         node = s.pop()
        #         inorder.append(node.val)
        #         node = node.right
        # print(inorder)
        # len_node = len(inorder)
        # i, j = 0, len_node - 1
        # while i <= j:
        #     if inorder[i] != inorder[j]:
        #         return False
        #     i += 1
        #     j -= 1
        # return True


if __name__ == '__main__':
    a1 = TreeNode(1)
    a2 = TreeNode(2)
    a3 = TreeNode(2)
    a4 = TreeNode(2)
    a5 = TreeNode(2)

    a1.left, a1.right = a2, a3
    a2.left = a4
    a3.left = a5
    print(Solution().isSymmetric(a1))
