class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1 :
            return [[1]]

        
        
        res = [[1]]
        for i in range(2, numRows+1):
            l = [1] 
            for j in range(0, len(res[-1])-1) :
                l.append(res[-1][j] + res[-1][j+1])
            l.append(1) 
            res.append(l)
            

        return res




        