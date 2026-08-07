class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj_set = {}
        for i, j in trust:
            adj_set[i] = adj_set.get(i, 0) + 1
            adj_set[j] = adj_set.get(j, 0)

        for i in adj_set.keys():
            if adj_set[i] == 0:
                return i

        return -1            