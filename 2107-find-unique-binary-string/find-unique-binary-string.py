class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # one line solution
        return ''.join(['1' if nums[i][i] is '0' else '0' for i in range(len(nums))])


        # explanation 
        '''
        ans = [] 
        for i in range(len(nums)):
            if nums[i][i] is '0' :
                ans.append('1')
            else:
                ans.append('0') 

        return ''.join(ans)

        '''
       
        