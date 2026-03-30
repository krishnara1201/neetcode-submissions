class Twitter:

    def __init__(self):
        self.userMap = defaultdict(set)
        self.postMap = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postMap[userId].append([tweetId, self.count])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []
        heapq.heapify(maxHeap)
        self.userMap[userId].add(userId)
        
        for followeeId in self.userMap[userId]:
            if followeeId in self.postMap:
                index = len(self.postMap[followeeId]) - 1
                tweetId, count = self.postMap[followeeId][index]
                heapq.heappush(maxHeap, [count, tweetId, followeeId, index - 1])

        while maxHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            if index >= 0:
                tweetId, count = self.postMap[followeeId][index]
                heapq.heappush(maxHeap, [count, tweetId, followeeId, index - 1])
        
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userMap[followerId]:
            self.userMap[followerId].remove(followeeId)
    