class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        n = len(people)
        people.sort()
        l, r = 0, n - 1

        while l <= r:
            if people[l] + people[r] == limit:
                l += 1
                
            r -= 1
            res += 1

        return res