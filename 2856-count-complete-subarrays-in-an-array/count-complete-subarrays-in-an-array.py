class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        ans = 0 
        dic = {} 
        i, j = 0, 0 
        while j < len(nums) :
            dic[nums[j]] = dic.get(nums[j] , 0 ) + 1 
            
            while (len(dic) == k ) :
                ans += len(nums) - j 
                dic [ nums [ i ]] -= 1
                if dic [ nums[i]] == 0 :
                    del dic[ nums[i]]

                i += 1
            j+=1
        
        return ans



        ''' BRURTE FORCE 
        for i in range(len(nums)):
            st = set() 
            for j in range(i, len(nums)):
                st.add(nums[j]) 
                if len(st) == k :
                    ans += 1
        return ans
        '''
        