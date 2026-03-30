class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        nums.sort(key=lambda x: (-count[x], -x))

        print(nums, count)

        res = []
        i = 0
        while k:
            if not res or res[-1] != nums[i]:
                res.append(nums[i])
                k -= 1
            i += 1

        return res