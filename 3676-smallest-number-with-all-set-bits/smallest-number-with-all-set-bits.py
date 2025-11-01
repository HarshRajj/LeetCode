class Solution:
    def smallestNumber(self, n: int) -> int:
        
        k = n.bit_length()
        return (1<<k)-1