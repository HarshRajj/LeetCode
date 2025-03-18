class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxln = 1 
        xor_sum = 0
        cur_sum = 0
        left = 0 

        for right in range(n):
            cur_sum += nums[right]
            xor_sum ^= nums[right]
            while xor_sum!= cur_sum :
                cur_sum -= nums[left] 
                xor_sum ^= nums[left] 
                left += 1 

            maxln = max(maxln, right-left + 1 )

        return maxln
