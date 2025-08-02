class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:

        counts = Counter(basket1)
        for k in basket2 :
            counts[k] -= 1 

        extra = [] 
        for key, val in counts.items() :
            if val%2 == 1 :
                return -1 
            for i in range( abs(val)//2 ) :
                extra.append(key) 

        if not extra :
            return 0 

        extra.sort() 

        mini = min ( min(basket1) , min(basket2)) 
        cost = 0

        for i in range(len(extra)//2) : 
            cost += min( extra[i] , 2* mini)

        return cost



        