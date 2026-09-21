import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)

        

        while len(heap) > 1:
            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)
            if a < b:
                val = b-a
                heapq.heappush(heap, -val)
            else:
                val = a-b
                heapq.heappush(heap, -val)
            
        return - heap[0]
        

        