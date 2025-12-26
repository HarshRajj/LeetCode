class Solution:
    def bestClosingTime(self, customers: str) -> int:
        best = 0 
        min_pen = 0
        pref = 0 

        for i in range(len(customers)):
            pref += -1 if customers[i] == 'Y' else 1 

            if pref < min_pen :
                best = i+1 
                min_pen = pref 


        return best
