class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        i = 0
        j = len(heights)-1 
        while i<j:
        
               
        
            area = (j-i)*min(heights[j],heights[i])
            max_water= max(max_water,area)
            if heights[i] > heights[j]:
                j-=1
            else :
                i+=1
         
        return max_water