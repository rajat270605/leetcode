import heapq as h
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        a = []
        heap = [(x*x + y*y,x,y) for x,y in points ]
        h.heapify(heap)

        while k > 0:
            distance, x, y = h.heappop(heap)
            a.append([x,y])
            k-=1

        return a 
            