class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        cum_shifts = [0] * (len(s) + 1) 

        for st, en, d in shifts: 
            if d == 0: 
                cum_shifts[st] -= 1 
                cum_shifts[en+1] += 1
            else: 
                cum_shifts[st] += 1
                cum_shifts[en+1] -= 1 

        cum_sum = 0
        s = list(s)
        for i in range(len(s)): 
            cum_sum += cum_shifts[i]

            new_code = (((ord(s[i]) + cum_sum) - 97) % 26) + 97 
            s[i] =  chr(new_code)
        
        return ''.join(s)





