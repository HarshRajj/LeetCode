class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1 
        maxi = 0
        while left < right :

            k = min(height[left] , height[right])
            ans = (right-left)*k 
            if ans > maxi :
                maxi = ans 
            if height[left]<height[right]:
                left+=1
                
            else :
                right-=1
        return maxi
                



        