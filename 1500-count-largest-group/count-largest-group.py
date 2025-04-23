class Solution:
    def countLargestGroup(self, n: int) -> int:
        sums = [0]*37
        for i in range(1,n+1) :
            summ = 0
            num = i 
            while i != 0 :
                summ += ( i % 10)
                i //= 10
            sums [summ] += 1

        maxlen = 0
        count = 0
        for i in sums :
            if i > maxlen :
                maxlen, count = i, 1
            elif i == maxlen :
                count+=1 
        return count        



        