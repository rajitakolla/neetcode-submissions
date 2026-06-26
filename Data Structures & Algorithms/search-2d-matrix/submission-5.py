class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, n

        required_row = 0

        if target > matrix[m-1][n-1]:
            return False

        while top <= bottom:
            print(matrix[top][n-1], top, n)
            if matrix[top][n-1] < target:
                top += 1
            else:
                required_row = top
                break
        print(required_row)
        start, end = 0, n-1

        while start <= end:
            mid = (start+end)//2

            if matrix[required_row][mid] < target:
                start = mid+1
            elif matrix[required_row][mid] > target:
                end = mid-1
            else:
                return True
        return False