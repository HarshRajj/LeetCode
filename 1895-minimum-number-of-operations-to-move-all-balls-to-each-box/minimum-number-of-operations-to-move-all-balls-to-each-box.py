class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0]*n

        for i in range(0,n):
            rightsum = 0
            for j in range(i+1,n):
                if boxes[j]=='1' :
                     
                    rightsum += abs(j-i)
            ans[i] = rightsum

        for i in range(n-1,-1,-1) :
            leftsum = 0
            for j in range(i-1,-1,-1):
                if boxes[j]=='1' :
                    leftsum += i-j 
            ans[i]+= leftsum
        return ans

            
