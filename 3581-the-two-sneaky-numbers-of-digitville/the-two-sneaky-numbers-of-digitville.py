class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        i = 0 
        while i<len(nums):
            correct = nums[i]
            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i] 
            else:
                i+= 1
            
        return [nums[-1], nums[-2]]
        