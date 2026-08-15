class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        left  = 0
        right = row*col -1
        while left<= right:

            m = (left+right)//2
            r = m//col
            c = m%col
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = m+1
            else:
                right = m-1
        return False