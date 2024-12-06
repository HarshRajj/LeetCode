class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        if start == target :
            return True 
        i = 0 
        j = 0 
        while i < n or j < n :
            while i<n and start[i] == '_' :
                    i+=1
            
            while j<n and target[j] == '_' :
                    j+=1

            if i<n and j<n :
                if start[i] != target[j]:
                    return False
                if start[i] =="R" and i>j :
                    return False 
                if start[i]=="L" and j>i :
                    return False
            i+=1
            j+=1
                            
        return i==j


        

        




        
        