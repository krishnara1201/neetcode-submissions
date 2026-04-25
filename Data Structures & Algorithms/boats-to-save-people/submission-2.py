class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        while l <= r:
            print(l,r, boats)
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            boats += 1
        return boats