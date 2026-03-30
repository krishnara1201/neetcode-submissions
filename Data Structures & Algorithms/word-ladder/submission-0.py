class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        adjset = {i:[] for i in wordList}
        
        for i in wordList:
            for j in wordList:
                if i == j or j in adjset[i]:
                    continue
                
                if self.word_comp(i,j):
                    adjset[i].append(j)
                    adjset[j].append(i)
        print(adjset)
        q = deque()
        q.append(beginWord)
        steps = 0
        visited = set()
        while q:
            qlen = len(q)
            steps += 1
            for i in range(qlen):
                word = q.popleft()
                if word == endWord:
                    return steps
                visited.add(word)
                for nei in adjset[word]:
                    if nei not in visited:
                        q.append(nei)
        return 0

    def word_comp(self, word1, word2):
        n = len(word1)
        for i in range(n):
            if word1[0:i] + "*" + word1[i+1:n] == word2[0:i] + "*" + word2[i+1:n]:
                print(word1[0:i] + "*" + word1[i+1:n])
                return True
        return False