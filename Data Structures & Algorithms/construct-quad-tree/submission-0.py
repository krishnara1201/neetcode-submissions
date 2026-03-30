"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        ROWS = len(grid)
        
        leafNode = {1:Node(1, True),
                    0:Node(0, True)}

        def dfs(n, r, c):
            if n == 1:
                return leafNode[grid[r][c]]
            
            n = n // 2
            topLeft = dfs(n, r, c)
            topRight = dfs(n, r, c + n)
            bottomLeft = dfs(n, r + n, c)
            bottomRight = dfs(n, r + n, c + n)

            if (topLeft.isLeaf and 
                topRight.isLeaf and
                bottomLeft.isLeaf and
                bottomRight.isLeaf and
                topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                return topLeft
            else:
                return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)

        return dfs(len(grid), 0, 0)