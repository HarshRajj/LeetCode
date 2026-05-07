class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1 
        leftmax = 0
        rightmax = 0 
        total = 0

        while l<r :
            if height[l] <= height[r] :
                if leftmax > height[l] :
                    total += leftmax - height[l]
                else :
                    leftmax = height[l]
                l+=1 
            else :
                if rightmax > height[r] :
                    total += rightmax - height[r]
                else :
                    rightmax = height[r]

                r-=1

        return total




        