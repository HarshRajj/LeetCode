import math
from collections import defaultdict
from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        lmt = math.isqrt(n)

        karr = defaultdict(list)
        
        # 1. Square Root Decomposition Phase
        for q in queries:
            l, r, k, v = q  # FIXED: added comma between k and v
            
            # Large jumps (k >= sqrt(n)): Direct simulation is fast enough (at most sqrt(n) steps)
            if k >= lmt:
                for i in range(l, r + 1, k):
                    nums[i] = (nums[i] * v) % MOD
            # Small jumps: Group them to process via Difference Array
            else:
                karr[k].append(q)

        # 2. Difference Array Phase (Only for small jumps)
        for k, query_list in karr.items(): 
            diff = [1] * n

            for q in query_list:
                l, r, _, v = q

                diff[l] = (diff[l] * v) % MOD
                steps = (r - l) // k   # FIXED: Changed 'step' to 'steps'
                nxt = l + (steps + 1) * k 
                
                if nxt < n:
                    # pow(v, -1, MOD) is valid in Python 3.8+ for modular inverse
                    diff[nxt] = (diff[nxt] * pow(v, -1, MOD)) % MOD

            # Resolve the difference array and apply to nums
            for i in range(n):
                if i >= k:
                    diff[i] = (diff[i] * diff[i - k]) % MOD
                
                # FIXED: Apply the resolved multiplier diff[i] instead of nums[i]
                if diff[i] != 1:
                    nums[i] = (nums[i] * diff[i]) % MOD

        # 3. Final XOR
        ans = 0 
        for num in nums:
            ans ^= num 

        return ans