class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        dic = defaultdict(int)
        rep = 0
        mis = 0
        n= len(grid)
        for row in grid :
            for k in row :
                dic [ k ]+=1 

        for k in range (1, n*n +1) :
            if dic [k] == 2 :
                rep = k 
            if dic[k] == 0 :
                mis = k 

        return [rep, mis]