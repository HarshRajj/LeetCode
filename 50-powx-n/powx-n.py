class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # Helper function for recursion
        def function(base=x, exponent=abs(n)):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                return function(base * base, exponent // 2)
            else:
                return base * function(base * base, (exponent - 1) // 2)
        
        # Compute the result
        f = function()

        # Handle positive and negative exponents
        return float(f) if n >= 0 else 1 / f