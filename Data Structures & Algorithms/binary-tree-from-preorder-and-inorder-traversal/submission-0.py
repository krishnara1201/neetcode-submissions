# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        indices = {}

        for ind, val in enumerate(inorder):
            indices[val] = ind
        
        p_index = 0
        def dfs(l, r):
            nonlocal p_index
            if l > r:
                return None
            val = preorder[p_index]
            
            p_index += 1
            root = TreeNode(val)
            mid = indices[val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
            
        return dfs(0, len(preorder) -1)
