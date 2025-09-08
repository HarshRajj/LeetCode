class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1,n+1):
            x = n-a
            y = n-x
            if '0' not in str(x) and '0' not in str(y):
                return [x,y]