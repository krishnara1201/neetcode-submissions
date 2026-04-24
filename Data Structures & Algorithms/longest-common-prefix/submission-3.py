class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.leaf = False
        self.hvchildren = False
        self.mult = False
    
    def add(self, root, string):
        curr = root
        for c in string:
            ind = ord(c) - ord('a')
            if not curr.children[ind]:
                curr.children[ind] = TrieNode()
                if curr.hvchildren:
                    curr.mult = True
                curr.hvchildren = True
            curr = curr.children[ind]
        curr.leaf = True

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = TrieNode()
        for s in strs:
            root.add(root, s)
        res = ""
        curr = root
        
        while curr.hvchildren and not curr.leaf:
            if curr.mult:
                break
            for i in range(26):
                if curr.children[i]:
                    res += chr(ord('a') + i)
                    curr = curr.children[i]
                    break

        return res
