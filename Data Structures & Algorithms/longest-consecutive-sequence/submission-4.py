class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        current = 1
        highest = 1 
        for i in range(1,len(nums)):
            if nums[i]== nums[i-1] +1 :
                current +=1
            elif nums[i]== nums[i-1]:
                continue  
            else:
                current = 1 
            highest = max(highest,current)
        return highest 