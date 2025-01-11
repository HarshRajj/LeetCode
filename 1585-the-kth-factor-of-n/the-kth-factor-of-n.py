class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        '''
        ans = [i for i in range(1,n//2+1) if n%i == 0] 
        ans.append(n)
        return ans[k-1] if k-1 < len(ans) else -1
        ''' 

        factor = [] 
        for i in range(1,int(n**0.5)+1) :
            if n%i == 0 :
                factor.append(i) 
                if i!= n//i :
                    factor.append(n//i) 

        factor.sort() 
        return factor[k-1] if k-1 < len(factor) else -1
        