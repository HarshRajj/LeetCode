# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy 

        while head :
            while head.next and head.val == head.next.val:
                head = head.next
            if prev.next == head :
                prev = prev.next 
            else :
                prev.next = head.next
            
            head = head.next 
        return dummy.next
            