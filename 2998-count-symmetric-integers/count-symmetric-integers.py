class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high+1) :
            num = str(i)
            if len(num)%2 == 0 :
                mid = len(num)//2 
                if sum(map(int, num[:mid])) == sum(map(int, num[mid:])) :
                    count+= 1 

        return count
                
        