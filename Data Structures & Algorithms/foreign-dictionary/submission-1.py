class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_dic = {c:set() for w in words for c in w}

        for i in range(len(words) -1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            j = 0
            while j < minLen:
                if w1[j] != w2[j]:
                    adj_dic[w1[j]].add(w2[j])
                    break
                j += 1

        visit = {}
        res = []

        def dfs(node):
            if node in visit:
                return visit[node]
            
            visit[node] = True

            for nei in adj_dic[node]:
                if dfs(nei):
                    return True
            
            visit[node] = False
            res.append(node)

        for c in adj_dic:
            if  dfs(c):
                return ""

        return "".join(reversed(res))
        

            

            
            
