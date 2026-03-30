# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        cache = {None:0}

        def dfs(root):
            if root in cache:
                return cache[root]
            cache[root] = root.val
            if root.left:
                cache[root] += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                cache[root] += dfs(root.right.left) + dfs(root.right.right)
            
            cache[root] = max(cache[root], dfs(root.left) + dfs(root.right))
            return cache[root]
        
        return dfs(root)
        # pre_order = {}
        # def preorder(root):
        #     if not root:
        #         return
        #     else:
        #         pre_order[index] = root
        #         index += 1
        #         preorder(root.left)
        #         preorder(root.right) 
        
        # n = len(pre_order)

        # return dfs(root, False)