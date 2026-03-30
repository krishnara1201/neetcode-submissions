class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        
        res = sorted(list(count.keys()), key=lambda x:-count[x])
        
        return res[:k]