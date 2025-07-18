# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow =head 
        fast = head 
        stk = []

        while fast and fast.next :
            stk.append(slow.val)
            slow = slow.next 
            fast = fast.next.next 

        if fast :
            slow = slow.next

        while slow!= None and stk :
            if not stk or stk.pop() != slow.val:
                return False
            slow = slow.next 
            

        return True  


        
        