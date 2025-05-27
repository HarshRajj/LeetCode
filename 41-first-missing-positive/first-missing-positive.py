class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n) :
            while 1<= nums[i] <= n and nums[ nums[i] -1] != nums[i] : 
                temp = nums[i]
                nums[i] = nums [ nums[i] - 1] 
                nums[temp - 1] = temp 

        for i in range(1, n+1):
            if i!= nums[i-1]:
                return i 

        return n+1




        