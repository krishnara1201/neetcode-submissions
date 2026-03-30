class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if strs[0][:i+1] != strs[j][:i+1]:
                    return prefix
            prefix = strs[0][:i+1]

        return prefix