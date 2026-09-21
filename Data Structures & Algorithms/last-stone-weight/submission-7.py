import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)

            val = a - b
            if val > 0:
                heapq.heappush(heap, -val)

        if heap:
            return -heap[0]
        return 0