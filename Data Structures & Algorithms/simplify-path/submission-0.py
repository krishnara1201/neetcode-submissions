class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        stack = []
        
        for i in path_list:
            if not i:
                continue
            elif i == ".":
                continue
            elif i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        
        return "/" + "/".join(stack)
                
        