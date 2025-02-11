# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self, root: Optional[TreeNode], ans)->List[int]:
        if root == None :
            return ans 
        else:
            ans.append(root.val)
            self.rec(root.left, ans)
            self.rec(root.right, ans)


    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.rec(root, ans)
        return ans
        
        
        
            
        