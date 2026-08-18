class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        

        count = Counter(nums)
        res = list(set(nums))
        res.sort(key = lambda x: -count[x])
        return res[:k]

        

                
        