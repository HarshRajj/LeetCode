# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ind, sum = 0, -inf 
        q = deque() 
        q.append(root)
        level = 1

        while q :
            ql = len(q)
            cur = 0

            for i in range(ql) :
                node = q.popleft() 
                cur += node.val 
                if node.left : q.append(node.left)
                if node.right : q.append(node.right)

            if cur > sum :
                ind = level
                sum = cur 
                
            level += 1

        return ind



        