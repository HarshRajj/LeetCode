class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def rev(n) : 
            ans = 0
            while n>0 :
                n, rem = divmod(n, 10)
                ans = 10 * ans + rem

            return ans
        dic = {}
        dist = inf
        for i, num in enumerate(nums):
            r = rev(num)
            if num in dic :
                dist = min(dist, i-dic[num])

            dic[r] = i 

        return -1 if dist == inf else dist


        