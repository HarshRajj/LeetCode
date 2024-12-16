class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n =len(matrix)
        actualSet = set(range(1,n+1))
        for row in matrix :
            if set(row)!= actualSet :
                return False 
        for col in zip(*matrix):
            if set(col)!= actualSet :
                return False
        return True
        
        



                
            
        