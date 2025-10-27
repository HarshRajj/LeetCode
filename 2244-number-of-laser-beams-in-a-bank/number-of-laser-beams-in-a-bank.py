class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        arr = []
        for b in bank :
            cnt = b.count('1') 
            arr.append(cnt) if cnt != 0 else None
        
        beams = 0 

        n = len(arr)
        if n ==1 :
            return beams 
        else :
            i = 0 
            while i < n-1 :
                beams += arr[i] * arr[i+1]
                i+=1 

        return beams
        