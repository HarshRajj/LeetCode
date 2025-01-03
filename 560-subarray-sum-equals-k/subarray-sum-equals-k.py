class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        dic = {0:1} 
        pr = 0 
        cnt = 0 
        for num in nums :
            pr += num
            x = pr-k 
            if x in dic :
                cnt += dic[x] 
            if pr in dic :
                dic[pr]+=1 
            else :
                dic[pr] = 1
        return cnt


        