class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        largest = 0
        for num in num_set:
            if num-1 not in num_set:
                streak = 1
                while num+1 in num_set:
                    num +=1
                    streak +=1
                largest = max(largest,streak)
        return largest

        