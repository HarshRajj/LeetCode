# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n  = len(postorder)
        postvalind = {} 
        for i , num in enumerate (postorder) :
            postvalind[num] = i 

        def build(i1, i2, j ) :
            if i1 > i2 :
                return None 
            
            root = TreeNode( preorder [ i1 ] ) 
            if i1 != i2 :
                left_val = preorder[ i1 + 1 ] 
                mid = postvalind[left_val] 
                leftsize = mid - j + 1
                root.left = build (i1 + 1 , i1+ leftsize , j )
                root.right = build (i1 + leftsize + 1 , i2 , mid+1 )
            return root  
        return build (0 , n-1, 0 )




        
        