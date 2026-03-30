# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val = val)
            
        curr = root
        prev = TreeNode()
        while curr:
            prev = curr
            if val > curr.val:
                curr = curr.right
            else:
                curr = curr.left

        if val > prev.val:
            prev.right = TreeNode(val = val)
        else:
            prev.left = TreeNode(val = val)

        return root