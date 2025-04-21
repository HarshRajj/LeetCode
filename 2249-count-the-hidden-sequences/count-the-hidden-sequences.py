class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        curr = 0 
        minval = 0
        maxval = 0 

        for d in differences :
            curr = curr + d 
            minval = min(minval, curr)
            maxval = max(curr, maxval) 

            if (upper-maxval) - (lower-minval) + 1 <=0 :
                return 0 
        
        return (upper-maxval) - (lower-minval) + 1