# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        if not head1 :
            return head2 
            
        if not head2:
            return head1 
        
        if head1.val < head2.val:
            head = head1
            cur1 = head1.next
            cur2 = head2 
            
        else :
            head = head2 
            cur2 = head2.next 
            cur1 = head1 
            
        cur = head 
        
        while cur1 and cur2 :
            if cur1.val < cur2.val :
                cur.next = cur1 
                cur1 = cur1.next 
                
            else:
                cur.next =  cur2
                cur2 = cur2.next 
            cur = cur.next    
                
        if cur1 :
            cur.next = cur1 
            
        if cur2 :
            cur.next = cur2
            
        return head

        