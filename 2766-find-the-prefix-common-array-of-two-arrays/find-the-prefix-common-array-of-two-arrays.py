class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans=0
        C=[]
        freq=[0]*len(A)
        for i in range(len(A)):
            if A[i]==B[i]:
                
                ans+=1
                C.append(ans)
                continue
            freq[A[i]-1]+=1
            freq[B[i]-1]+=1
            if freq[A[i]-1]==2:
                ans+=1
            if freq[B[i]-1]==2:
                ans+=1
            C.append(ans)
        return C
            


            
            

        