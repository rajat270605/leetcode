class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        for num in nums:
            count[num] = count.get(num,0) +1

        data = list(count.items())
        result = sorted(data, key=lambda x: x[1], reverse=True)
        print(result[:k])
        return [item[0] for item in result[:k]]