class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        ans=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)) :
                prod = nums[i]*nums[j]

                ans+=8*dic[prod]
                
                dic[prod] += 1

               
        return ans 