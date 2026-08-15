class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        answer = r

        while l <= r:

            mid = (l + r) // 2

            totalHours = 0

            for pile in piles:
                totalHours += (pile + mid - 1) // mid

            if totalHours <= h:
                answer = mid
                r = mid - 1
            else:
                l = mid + 1

        return answer