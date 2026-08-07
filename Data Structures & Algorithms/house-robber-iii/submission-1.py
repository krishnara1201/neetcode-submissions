# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, choice):
            if not root:
                return 0
            elif choice:
                return dfs(root.left, False) + dfs(root.right, False)
            else:
                return max(dfs(root.left, False) + dfs(root.right, False), root.val + dfs(root.left, True) + dfs(root.right, True))
        
        dfs(root, False)
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