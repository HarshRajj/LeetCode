class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        rowf = [0]*m
        colf = [0]*n 
        has={}
        for i in range(m):
            for j in range(n):
                
                has[mat[i][j]]=[i,j]
        
        for i in range(len(arr)):
            ro = has[arr[i]]
            rowf[ro[0]] += 1
            colf[ro[1]] += 1 

            if rowf[ro[0]]==n :
                return i 

            if colf[ro[1]] == m :
                return i 

            

         
            

        
                    


            

            
        
        