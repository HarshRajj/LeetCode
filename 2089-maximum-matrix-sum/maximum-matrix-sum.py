class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        mini = float('inf')
        neg = 0
        totalSum = 0
        for i in range(n):
            for j in range(n) :
                k = matrix[i][j]
                if k < 0 : neg += 1
                ab = abs(k)
                totalSum += ab
                if ab < mini : mini = ab
        return totalSum if neg%2 == 0 else totalSum-(2*mini)
        

        