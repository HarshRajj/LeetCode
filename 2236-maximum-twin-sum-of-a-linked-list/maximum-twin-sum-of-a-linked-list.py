# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head 
        fast = head 

        while fast and fast.next :
            fast = fast.next.next 
            slow = slow.next 

        cur, prev = slow, None 
        
        while cur:
            next_node = cur.next    
            cur.next = prev
            prev = cur
            cur = next_node

        maxim = 0

        while prev :
            maxim = max(maxim, head.val + prev.val)
            prev = prev.next 
            head = head.next 

        return maxim
        