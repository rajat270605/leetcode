class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []          # (start_index, height)
        max_area = 0

        for i in range(len(heights)):
            start = i

            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                width = i - index
                max_area = max(max_area, height * width)

                start = index

            stack.append((start, heights[i]))

        while stack:
            index, height = stack.pop()
            width = len(heights) - index
            max_area = max(max_area, height * width)

        return max_area