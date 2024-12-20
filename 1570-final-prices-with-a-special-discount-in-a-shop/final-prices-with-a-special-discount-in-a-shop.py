class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range (len(prices)) :
            j = i+1 
            while j < len(prices) and prices[i] < prices[j]:
                j+=1 
            if j < len(prices) and prices[i] >= prices[j] :
                prices[i]-= prices[j] 
        return prices
        

        

            

        

        