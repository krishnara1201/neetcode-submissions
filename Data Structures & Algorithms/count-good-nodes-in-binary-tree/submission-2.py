# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 0
        def dfs(root, max_prev):
            nonlocal count
            if not root:
                return
            if root.val >= max_prev:
                count += 1
                max_val = root.val
            else:
                max_val = max_prev
            
            left = dfs(root.left, max_val)
            right = dfs(root.right, max_val)

            return 
        dfs(root, root.val)
        return count