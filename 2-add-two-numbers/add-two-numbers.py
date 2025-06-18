# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1, None)
        t1 = l1
        t2 = l2
        curr = dummy 
        carry = 0
        while t1!= None or t2!= None :
            summ = carry 
            if t1 :
                summ += t1.val
            if t2 :
                summ += t2.val 

            newNode = ListNode(summ % 10) 
            carry = summ //10 
            curr.next = newNode 
            curr = curr.next 

            if t1 :
                t1 = t1.next 
            if t2 :
                t2 = t2.next 

        if carry :
            newNode = ListNode(carry) 
            curr.next  = newNode 

        return dummy.next  


        