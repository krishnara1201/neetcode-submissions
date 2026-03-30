# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ret = []

        def dfs(root):
            if not root:
                ret.append("%")
                return 
            
            ret.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        print("#".join(ret))
        return "#".join(ret)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        dat = data.split("#")
        q = deque(dat)

        def dfs(q):
            print(q)
            if not q:
                return None

            node = None
            print(q[0])


            if q[0] == "%":
                q.popleft()
                
            else:
                num = q.popleft()
                node = TreeNode(int(num))
                print("left")
                node.left = dfs(q)
                print("right")
                node.right = dfs(q)

            print(node)
            return node
        res = dfs(q)
        print(res)
        return res
        

