class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        lucky = -1
        maxim = -1

        for key, val in freq.items() :
            if key == val :
                lucky = key 
            maxim = max(lucky, maxim)

        return maxim
                
        