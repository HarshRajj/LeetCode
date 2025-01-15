class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        setbits = bin(num2).count('1')  # Count of set bits in num2
        res = 0

        # First loop: Use the set bits in num1 from high to low
        for i in range(31, -1, -1):
            if num1 & (1 << i):
                res |= (1 << i)
                setbits -= 1
            if setbits == 0:
                break

        # Second loop: Set the remaining bits from low to high
        for i in range(32):
            if setbits == 0:
                break
            if not (res & (1 << i)):  # If the bit is not already set
                res |= (1 << i)
                setbits -= 1

        return res


        