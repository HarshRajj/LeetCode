class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n, i = len(bits), 0 
        
        while i<n-1 :
            if bits[i] == 1 :
                i+=2
            else :
                i+=1
        
        return i == n-1