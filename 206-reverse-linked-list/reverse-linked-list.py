# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        '''
        temp = head 
        stk = []
        while temp != None :
            stk.append(temp.val)
            temp = temp.next 

        temp = head 
        while temp!=None :
            temp.val = stk.pop() 
            temp = temp.next

        '''
        # METHOD 2 
        temp = head 
        prev = None 
        while temp!= None :
            front = temp.next 
            temp.next = prev 
            prev = temp 
            temp = front 
            

        return prev

        
        