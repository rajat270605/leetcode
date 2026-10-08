import heapq as h

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        h.heapify(heap)

        while len(heap) > 1:
            a = -h.heappop(heap)
            b = -h.heappop(heap)

            val = a-b
            if val >0:
                h.heappush(heap,-val)
            
        if heap:
            return -heap[0]
        return 0
        