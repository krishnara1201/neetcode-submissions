class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()

        for i in range(k):
            while q and nums[i] > q[-1]:
                q.pop()
            q.append(nums[i])
        # print(q)
        res = []
        if q:
            res.append(q[0])

        l = 0
        for r in range(k, len(nums)):
            # print(q, l, r)
            while q and nums[r] > q[-1]:
                # print(nums[r],  q[-1])
                q.pop()
            q.append(nums[r])
            # print(q)
            if nums[l] == q[0]:
                q.popleft()
            
            res.append(q[0])
            l += 1
        
        return res