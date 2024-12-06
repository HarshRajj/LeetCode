class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in range(0,len(arr)):
            if  arr[i] <= k :
                k+=1 
            else :
                break 
        return k
        