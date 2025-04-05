class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.total = 0 
        def dfs ( index : int , cur_xor : int) :
            if index == len(nums) :
                self.total += cur_xor 
                return 

            dfs(index+1, cur_xor ^ nums[index]) 
            dfs(index+1, cur_xor) 

        dfs(0,0)
        return self.total
        


        