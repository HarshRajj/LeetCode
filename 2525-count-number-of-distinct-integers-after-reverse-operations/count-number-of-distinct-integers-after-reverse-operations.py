class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        a=set()
        for i in nums:
            a.add(i)
           
            a.add(int(str(i)[::-1]))
        return len(a)



        