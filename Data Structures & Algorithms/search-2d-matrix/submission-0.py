class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix) -1

        while t < b:
            m = (t+b)//2
            if target < matrix[m][0]:
                b = m-1
            elif target > matrix[m][-1]:
                t = m+1
            else:
                break
        row = (t + b) // 2

        l =0
        r = len(matrix[row])-1
        while l<= r:
            mid = (l+r)//2
            
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] <  target:
                l = mid+1
            else:
                r = mid-1
        return False
