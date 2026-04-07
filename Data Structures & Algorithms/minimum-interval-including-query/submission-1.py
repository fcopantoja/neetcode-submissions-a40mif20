class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        result = []
        

        for query in queries:
            heap = []
            for interval in intervals:
                if query in range(interval[0], interval[1] + 1):
                    distance = interval[1] - interval[0] + 1
                    heapq.heappush(heap, (distance, interval[0], interval[1]))
            
            if not heap:
                result.append(-1)
            else:
                distance, start, end = heapq.heappop(heap)
                result.append(distance)

        return result
            
                

