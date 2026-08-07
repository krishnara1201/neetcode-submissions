# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        max_diameter = 1

        max_diameter =  2 + self.diameterOfBinaryTree(root.left) + self.diameterOfBinary(root.right)