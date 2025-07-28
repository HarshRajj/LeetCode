from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        idx = {}
        maxi = 0
        current_sum = 0
        start = 0  # The only new variable needed for optimization

        for i in range(len(nums)):
            # If a duplicate is found that is part of our current window
            if nums[i] in idx and idx[nums[i]] >= start:
                # Find the position of the previous duplicate
                prev_idx = idx[nums[i]]
                
                # Instead of resetting, subtract the values from the left of the
                # window until the old duplicate is gone.
                for j in range(start, prev_idx + 1):
                    current_sum -= nums[j]
                
                # Slide the window's start forward
                start = prev_idx + 1

            # Add the current element to the window and update its index
            current_sum += nums[i]
            idx[nums[i]] = i
            
            # Update the maximum sum found so far
            maxi = max(maxi, current_sum)
            
        return maxi