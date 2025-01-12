class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        onerow = [0]*m
        onecol = [0]*n
        for i in range(m) :

            for j in range(n):
                if grid[i][j] == 1 :
                   onerow[i] += 1 
                   onecol[j] += 1 

        for i in range(m):
            for j in range(n):
                grid[i][j] = onerow[i]+onecol[j] - (m-onerow[i]) - (n-onecol[j])

        return grid
            
