class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0]*n 
        leftcost = 0 
        leftcnt = 0 
        rightcost = 0 
        rightcnt = 0 

        for i in range(1,n):
            if boxes[i-1]=='1' :
                leftcnt +=1 
            leftcost += leftcnt 
            ans[i] = leftcost 

        for i in range(n-2,-1,-1) :
            if boxes[i+1] == '1' :
                rightcnt+=1 
            rightcost += rightcnt 
            ans[i]+= rightcost
        
        return ans




            
