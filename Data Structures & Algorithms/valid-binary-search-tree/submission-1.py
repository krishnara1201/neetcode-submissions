# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, minval, maxval):
            if not(root):
                return [True, minval, maxval]
            if root.val == minval or root.val == maxval:
                return [False, 0, 0]

            left = dfs(root.left, root.val, root.val)
            right = dfs(root.right, root.val, root.val)
            
            
            if not(left[0] or right[0]):
                return [False, 0, 0]
            
            elif left[2] > root.val or right[1] < root.val:
                return [False, 0, 0]
            else:
                return [True, left[1], right[2]]

        return dfs(root, 1001, -1001)[0]

