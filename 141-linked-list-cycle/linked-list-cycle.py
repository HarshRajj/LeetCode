# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        '''
        temp = head 
        if not head :
            return False
        if head.next == None :
            return False
        dic = {}
        while temp!= None :
            if temp in dic :
                return True 
            else :
                dic[temp] = 1

            temp = temp.next

        return False
        '''

        # APPROACH 2 : HARE AND TORTOISE

        slow = head
        fast = head 
        while fast!= None and fast.next!= None :
            

            slow = slow.next 
            fast = fast.next.next
            if slow == fast :
                return True 

        return False




        