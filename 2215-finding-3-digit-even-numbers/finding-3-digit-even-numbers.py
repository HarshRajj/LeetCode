class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = Counter(digits)
        ans = [] 
        for num in range(100 ,999, 2) :
            tmp = num 
            dic = {} 
            while tmp > 0 :
                r = tmp%10 
                dic[r] = dic.get(r, 0) + 1 
                tmp //= 10 

            flag = True 
            for x in dic : 
                if dic[x] > freq[x] :
                    flag = False 
                    break 

            if flag : 
                ans.append(num) 

        return ans


        