# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        cur = head

        fhead = ListNode(0)
        ftail = fhead 

        shead = ListNode(0)
        stail = shead 

        while cur :
            if cur.val < x :
                ftail.next = ListNode(cur.val)
                ftail = ftail.next
            else:
                stail.next = ListNode(cur.val)
                stail = stail.next 

            cur = cur.next 

        ftail.next = shead.next 

        return fhead.next



        '''

        def array_to_linked_list(arr):
            if not arr:
                return None
            head = ListNode(arr[0])
            current = head
            for val in arr[1:]:
                current.next = ListNode(val)
                current = current.next
            return head


        if not head :
            return head 
        if not head.next :
            return head 

        arr1 = []
        arr2 = [] 

        while head :
            if head.val < x:
                arr1.append(head.val)
            else:
                arr2.append(head.val)
            head = head.next 

        p = array_to_linked_list(arr1)
        q = array_to_linked_list(arr2)

        head = p
        while p and p.next :
            p = p.next 
        if p!= None:
            p.next = q 
        else:
            head = q


        return head
        '''
    




        