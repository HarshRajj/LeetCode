class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        def divisors(num):
            div = []
            for i in range(2,int(math.sqrt(num))+1) :
                if num % i == 0 :
                    div.append(i)
                    if i != num//i : div.append(num//i)
                    

            return div 
        ans =  0
        # return divisors(nums[-1])
        for num in nums :
            divs = []
            divs = divisors(num)
            if len(divs) == 2 :
                ans =  ans + num + 1 + sum(divs)

        return ans





        