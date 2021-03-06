# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None: return None
        if root.left == None or root.right == None:
            if root.val >= val and root.left == None:
                root.left = TreeNode(val)
                return root
            if root.val < val and root.right == None:
                root.right = TreeNode(val)
                return root
        if root.val <= val: root.right = self.insertIntoBST(root.right, val)
        if root.val > val: root.left = self.insertIntoBST(root.left, val)
        return root