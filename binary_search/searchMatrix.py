class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS = len(matrix); COLS = len(matrix[0])
        l = 0; r = ROWS*COLS-1

        while l <= r:
            m = l + (r-l) // 2
            rw = m // COLS; cl = m % COLS

            if matrix[rw][cl] > target:
                r = m - 1
            elif matrix[rw][cl] < target:
                l = m + 1
            else:
                return True 
        return False

if __name__ == '__main__':
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target = 3

    s = Solution()
    res = s.searchMatrix(matrix, target)  # Output: True
    print(res)