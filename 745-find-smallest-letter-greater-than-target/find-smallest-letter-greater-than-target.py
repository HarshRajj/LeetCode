class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        l = 0
        r = n-1 
        pos = -1
        while l <= r :
            mid = (r-l) + l //2 

            if letters[mid]>target :
                pos = mid
                r = mid - 1 

            elif letters[mid]<= target :
                l = mid+1

        if pos == -1 :
            return letters[0]
        
        return letters[pos]
        