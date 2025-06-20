class Solution:
    def maxDistance(self, string: str, k: int) -> int:
        n, s, e, w = 0, 0, 0, 0
        maxi = 0
        for i in range(len(string)) :
            if string[i] == "N" :
                n +=1
            elif string[i] == "S" :
                s += 1
            elif string[i] == "E":
                e += 1
            else :
                w += 1

            bs = abs(e-w) + abs(n-s) 
            extra = min (2*k, i+1-bs) 
            total = bs + extra 

            maxi = max(maxi, total)

        return maxi
        
        


        
        

        
            
            
        
        