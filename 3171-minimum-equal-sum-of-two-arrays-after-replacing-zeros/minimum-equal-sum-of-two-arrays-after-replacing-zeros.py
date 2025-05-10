class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zeroes1 = 0
        zeroes2 = 0 
        sum1 = 0
        sum2 = 0
        for num in nums1 :
            sum1 += num
            if num == 0 :
                zeroes1 += 1


        for num in nums2 :
            sum2 += num 
            if num == 0 :
                zeroes2 += 1

        if zeroes1 == 0 and sum1 < sum2 + zeroes2 :
            return -1 
        if zeroes2 == 0 and sum2 < sum1 + zeroes1 :
            return -1 

        return max(sum1 + zeroes1, sum2 + zeroes2) 


        
        


        