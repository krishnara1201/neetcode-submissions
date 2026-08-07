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
            
            ret.append("#" + str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        print("".join(ret))
        return "".join(ret)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        q = deque(list(data))

        def dfs(q):
            if not q:
                return

            node = None
            print(q[0])
            if q[0] != "%":
                q.popleft()
                num = ""
                while q and (q[0] != "%" and q[0] != "#"):
                    # print(q[0])
                    val = q.popleft()
                    num += val

                print(num, q)
                node = TreeNode(int(num))
                q.popleft()
            else:
                q.popleft()

            if node:
                node.left = dfs(q)
                node.right = dfs(q)

            return node

        return dfs(q)
        

