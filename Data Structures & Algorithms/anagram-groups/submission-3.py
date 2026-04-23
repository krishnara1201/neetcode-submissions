class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for s in strs:
            key = [0] * 27
            for c in s:
                key[ord(c)-ord('a')] += 1
            dic[tuple(key)].append(s)
        return list(dic.values())