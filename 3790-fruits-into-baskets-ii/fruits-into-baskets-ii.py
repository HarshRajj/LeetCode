class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for fruit in fruits :
            j = 0
            while j<len(baskets) :
                cap = baskets[j]
                if cap >= fruit : 
                    baskets[j] = -1 
                    break 
                j += 1 
        cnt = 0
        for i in baskets :
            if i!= -1 :
                cnt += 1
                    
        return cnt
        