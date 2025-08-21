class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        h = [0] * cols
        res = 0
        for i in range(rows):
            for j in range(cols):
                h[j] = h[j] + 1 if mat[i][j] else 0
            for j in range(cols):
                min_height, l = h[j], j
                while 0 <= l and min_height:
                    min_height = min(min_height, h[l])
                    res += min_height
                    l -= 1
        return res