class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        '''brute---

        pos, neg = 0, 0
        for i in nums:
            if i<0 :
                neg+=1 
            if i>0 :
                pos+=1 

        return max(neg, pos)

        '''

        # Binary Search -----

        n = len(nums)
        start = 0
        end = n-1 
        while start <= end :
            mid = (start+end)//2 
            if nums[mid] > 0 :
                end = mid - 1 
            else:
                start = mid+1 

        pos = n-start

        start = 0
        end = n-1 
        while start<= end :
            mid = (start+end)//2
            if nums[mid]<0 :
                start = mid+1 
            else:
                end = mid-1 

        neg = end+1 

        return max(pos, neg)

        

        


        

        