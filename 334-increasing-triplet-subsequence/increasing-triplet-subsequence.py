class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n1 = float('inf')
        n2 = float('inf')

        for num in nums :
        
            if n1>= num :
                n1 = num
            elif n2>= num :
                n2 = num 

            else :
                return True 

        return False

        