# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root == None :
            return ans 

        q = deque() 
        q.append(root)
        while q :
            sz = len(q)
            lev = []

            for _ in range(sz) : 
                nod = q.popleft()
                if nod.left :
                    q.append(nod.left)
                if nod.right :
                    q.append(nod.right)

                lev.append(nod.val)
            ans.append(lev)

        return ans

        