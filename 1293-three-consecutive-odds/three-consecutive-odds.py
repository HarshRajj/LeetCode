class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i = 0
        n = len(arr)
        
        while (i<n) :
            c = 0
            while i<n and arr[i] % 2 == 1 :
                c += 1 
                if c == 3 :
                    return True 
                i+=1
            i+=1

        return False
        