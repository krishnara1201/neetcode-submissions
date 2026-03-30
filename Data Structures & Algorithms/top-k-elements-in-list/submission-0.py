class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        res = []

        frequency = [[] for i in range(len(nums) + 1)]
        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1
        
        for val, freq in hash_map.items():
            frequency[freq].append(val)
        
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                res.append(num)
                if k == len(res):
                    return res
                
        