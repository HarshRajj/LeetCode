class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        r = len(matrix)
        c = len(matrix[0])

        res = 0 
        for i in range(r) :
            for j in range(c):
                if matrix[i][j] == 1 and i>0 and j>0 :
                    matrix[i][j] = min(
                        matrix[i-1][j],
                        matrix[i][j-1],
                        matrix[i-1][j-1]
                    ) + 1

                res += matrix[i][j] 

        return res
            
        