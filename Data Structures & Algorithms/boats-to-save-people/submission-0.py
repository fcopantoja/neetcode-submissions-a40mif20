class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r = len(people) - 1
        result = []

        people.sort()

        while l <= r:
            if people[l] + people[r] <= limit:
                result.append([people[l], people[r]])
                l += 1
                r -= 1
            else:
                result.append([people[r]])
                r -= 1


        return len(result)