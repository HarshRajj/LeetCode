class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()

        a = nums[0]
        b = nums[1]
        c = nums[2]

        if a==b and b==c :
            return "equilateral" 
        if a+b > c :
            if a==b or b==c or a==c :
                return "isosceles"
            if a!=b and b!=c and a!=c :
                return "scalene"

        return "none"

        

        