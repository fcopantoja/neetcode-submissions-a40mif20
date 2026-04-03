class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        curr_passengers = trips[0][0]

        for i in range(1, len(trips)):
            if trips[i][1] < trips[i - 1][2]: #Overlapping
                curr_passengers += trips[i][0]
                if curr_passengers > capacity:
                    return False
            else:
                curr_passengers -= trips[i - 1][0] 
                curr_passengers += trips[i][0] 

        return True