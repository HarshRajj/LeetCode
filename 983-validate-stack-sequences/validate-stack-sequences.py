class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        j = 0
        for i in range(len(pushed)) :
            
            stk.append(pushed[i]) 
                
            while stk and stk[-1] == popped[j]:
                
                stk.pop()
                j+=1
        if not stk :
            return True
        else:
            return False
                