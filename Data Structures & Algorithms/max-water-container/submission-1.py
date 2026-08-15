class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                area = ((j-i)*min(heights[i],heights[j]))
                max_water = max(max_water,area)
        return max_water
        