class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:

        ans = [0]* (2*n - 1) 
        visited = [False]*(n+1) 
        
        def backtrack( ind , ans, used ) -> bool : 
            
            while ind < len(ans) and ans[ind]!=0 :
                ind += 1

            if ind == len(ans) :
                return True

            for i in range(n,0,-1) :
                if used[i] :
                    continue 
                if i == 1 :
                    ans[ind] = i 
                    used[i] = True 

                    if backtrack(ind+1, ans, used) :
                        return True 
                    used[i] = False
                    ans[ind] = 0 

                elif ind+i < len(ans) and ans[ind+i] == 0 :
                    ans[ind] = i 
                    ans[ind+i] = i 
                    used[i] = True 

                    if backtrack ( ind+1 , ans, used) :
                        return True 
                    used[i] = False 
                    ans[ind] = 0
                    ans[ind+i] = 0 

            return False 

        backtrack ( 0 , ans, visited) 
        return ans

        