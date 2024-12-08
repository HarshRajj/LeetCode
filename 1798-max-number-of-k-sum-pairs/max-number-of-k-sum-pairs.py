class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import Counter

        
        counts = Counter(nums)
        c = 0

        for num in counts:
            complement = k - num
            if complement in counts:
                if complement == num:
                    
                    c += counts[num] // 2
                else:
                    
                    c += min(counts[num], counts[complement])

                
                counts[complement] = 0
                counts[num] = 0
        return c


            


        
            
            


        
           
        


