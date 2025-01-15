class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bits1 = bin(num1).count("1")
        bits2 = bin(num2).count("1")

        if bits1 == bits2:
            return num1
        
        if bits1 > bits2:
            r = num1
            remove = bits1 - bits2
            x = 1
            while remove > 0:
                if r & x > 0:
                    r ^= x
                    remove -= 1
                x <<= 1
            return r
        
        if bits1 < bits2:
            r = num1
            add = bits2 - bits1
            x = 1
            while add > 0:
                if r & x == 0:
                    r |= x
                    add -= 1
                x <<= 1
            return r


        