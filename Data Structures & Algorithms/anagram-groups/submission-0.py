class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for st in strs:
            countL = [0] * 26
            for c in st:
                countL[ord(c) - ord('a')] += 1
            res[tuple(countL)].append(st)
        return list(res.values())