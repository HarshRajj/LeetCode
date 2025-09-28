class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort() 
        n = len(nums)

        for i in range (n-1, 1, -1):
            a = nums[i-2]
            b = nums[i-1]
            c = nums[i]
            if (a+b > c) :
                return a+b+c 

        return 0

        