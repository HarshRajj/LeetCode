# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def solve(root:Optional[TreeNode])-> List : 
            if root == None :
                return [0, None]
            l = solve(root.left)
            r = solve(root.right) 

            if l[0]== r[0] :
                return [l[0]+1, root] 
            elif l[0] > r[0] :
                return [l[0]+1, l[1]] 
            else :
                return [r[0]+1, r[1]]
            
            
        ans = solve(root)[1]
        return ans    
        