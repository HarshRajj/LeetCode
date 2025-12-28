class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        cnt = 0
        row = 0
        col = c-1

        while row<r and col >= 0 :
            if grid[row][col] < 0 :
                cnt += r-row
                col -= 1
            else:
                row += 1

        return cnt
        