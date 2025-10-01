class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        filled = 0 
        empty = numBottles
        ans = numBottles
        while empty >= numExchange :
            filled = empty // numExchange 
            empty = empty % numExchange
            ans += filled
            empty += filled 
            

        return ans

        



        