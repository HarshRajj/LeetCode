class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        even = 0
        odd = 0 
        for x in nums :
            if x%2 == 1 :
                odd += 1
            else:
                even += 1

        parity = nums[0]%2 
        alt = 1
        
        for i in range(1, n):
            cur_par = nums[i]%2
            if parity != cur_par :
                alt += 1
                parity = cur_par 

        
        return max(odd, even, alt)
        
    