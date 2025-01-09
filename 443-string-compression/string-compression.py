class Solution:
    def compress(self, chars: List[str]) -> int:
        
        idx = 0
        j = 0
        n = len(chars)
        count = 1
        if n == 1 :
            return 1
        while j<n :
            k = chars[j]
            count = 0
            
            while j < n and chars[j] == k:
                count+=1 
                j+=1
                
            chars[idx] = k
            idx+=1

            if count > 1 :
                for x in str(count):
                    chars[idx] = x 
                    idx+=1
            
        return idx





                

            


        
        