class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = len(nums)
        x = nums[0]
        res = []
        if x == 0 :
            res.append(True)
        else:
            res.append(False)
        for i in range(1,n) :
            x = 2*x + nums[i]

            if x % 5 == 0 :
                res.append(True)
            else:
                res.append(False)
        return res

            


        