class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(61):
            target = num1 - num2 * i
            if target >= 0 and target.bit_count() <= i <= target:
                return i
        
        return -1
        