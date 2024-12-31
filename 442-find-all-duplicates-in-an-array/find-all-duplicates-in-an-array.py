class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''
        ans = []
        for i in range(len(nums)):
            ind = abs(nums[i]) - 1  
            if nums[ind] < 0:  
                ans.append(ind + 1)
            else:
                nums[ind] *= -1  
        return ans

        '''

        ans = []
        checkset = set() 
        for i in nums :
            if i in checkset :
                ans.append(i)
            else :
                checkset.add(i)
        return ans