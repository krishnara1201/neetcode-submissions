# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False

        if self.sameTree(root, subRoot):
            return True
        else:
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)

            return left or right
        
        
        
    def sameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        if root1 and root2 and root1.val == root2.val:
            return (self.sameTree(root1.left, root2.left)) and (self.sameTree(root1.right, root2.right))
        else:
            return False
        