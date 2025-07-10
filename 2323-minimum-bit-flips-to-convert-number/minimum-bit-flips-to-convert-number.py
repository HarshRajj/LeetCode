class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        ''' no of flip bits are the number of set bits in XOR of the start and goal 
         why ???
         XOR means 1 if bits are different and 0 if bits are same, 
         if at any index, the XOR is one , it means bits were flipped at that index 
        '''

        ans = start^goal 
        count = 0

        for i in range(31):
            if ans & (1<<i) :
                count +=1

        return count


        