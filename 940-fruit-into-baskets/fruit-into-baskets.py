class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        dic = defaultdict(int)
        left = 0
        maxi = 0

        for right, fruit in enumerate(fruits) :
            dic[fruit] += 1

            while len(dic)>2 :
                leftfruit = fruits[left]
                dic[leftfruit]-=1

                if dic[leftfruit] == 0 :
                    del dic[leftfruit]
                left += 1

            maxi = max(maxi, right-left+1)

        return maxi

       
            

            


        

        