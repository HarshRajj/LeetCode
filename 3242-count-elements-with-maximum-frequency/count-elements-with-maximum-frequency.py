class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq_map = Counter(nums)
        maxi  = -1
        ans = 0
        for freq,val in freq_map.items() :
            if val>maxi :
                maxi = val
        
        for freq, val in freq_map.items() :
            if val == maxi :
                ans += val 
        return ans

        