class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        
        b, t = 0, n - 1
        
        mid = 0
        while b <= t:
            mid = b + (t-b)//2
            if (matrix[mid][0] <= target) and (matrix[mid][m-1] >= target):
                break

            if matrix[mid][0] > target:
                t = mid - 1
            if matrix[mid][m - 1] < target:
                b = mid + 1
        
       
        l, r = 0, m - 1

        while l <= r:
            row_mid = l + (r-l)//2
            if matrix[mid][row_mid] == target:
                return True
            if matrix[mid][row_mid] > target:
                r = row_mid - 1
            if matrix[mid][row_mid] < target:
                l = row_mid + 1

        return False