# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7 
        self.subtree_sums = [] 
        def dfs(node: TreeNode):
            if not node :
                return 0 
            s = node.val + dfs(node.left) + dfs(node.right)
            self.subtree_sums.append(s)
            return s

        total= dfs(root)
        max_prod = 0 
        for s in self.subtree_sums :
            max_prod = max(max_prod, s*(total-s))

        return max_prod % MOD
        