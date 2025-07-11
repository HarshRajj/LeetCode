class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n1 = float('inf')
        n2 = float('inf')

        for num in nums :
            n3 = num 

            if n1>= n3 :
                n1 = n3
            elif n2>= n3 :
                n2 = n3 

            else :
                return True 

        return False

        