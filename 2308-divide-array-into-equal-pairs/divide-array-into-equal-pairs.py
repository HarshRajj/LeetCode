class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        dic = Counter(nums) 
        for val in dic.values():
            if val%2 != 0:
                return False 

        return True

        '''
        nums.sort() 
        for i in range(0, len(nums)-1, 2):
            if nums[i] != nums[i+1]:
                return False 

        return True
        '''
        