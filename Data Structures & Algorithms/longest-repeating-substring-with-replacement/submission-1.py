class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        n = len(s)
        l = 0
        r = 0
        count ={}
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) +1

            
            greatest = max(count.values())

            while (r-l +1)- greatest > k :
                count[s[l]] -=1
                l +=1

            max_length = max(max_length,r-l+1)

        return max_length
