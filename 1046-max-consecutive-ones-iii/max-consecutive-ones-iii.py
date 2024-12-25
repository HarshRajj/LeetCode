class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        end = 0
        count = 0
        ma = 0
        n = len(nums)

        while end < n:
            if nums[end] == 0:
                count += 1

    
            while count > k:
                if nums[start] == 0:
                    count -= 1
                start += 1

            ma = max(ma, end - start + 1)

            
            end += 1

        return ma



        

                
                

            
        