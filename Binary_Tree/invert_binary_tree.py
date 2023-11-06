# 226. Invert Binary Tree


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root):
        if root == None:
            return

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.right)
        self.invertTree(root.left)

        return root
