# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseLL(self, head: Optional[ListNode] )-> Optional[ListNode] :
        temp = head 
        prev = None 
        while temp!= None :
            front = temp.next 
            temp.next = prev 
            prev = temp 
            temp = front 
        return prev

    def getKth(self, temp, k):
        k -= 1
        while temp is not None and k>0 :
            k-= 1
            temp = temp.next

        return temp

            

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head 
        prevLast = None

        while temp!= None :
            Kth = self.getKth(temp, k)
            if Kth is None :
                if prevLast :
                    prevLast.next = temp
                break 
            nextNode = Kth.next 
            Kth.next = None
            self.reverseLL(temp)
            if temp == head :
                head = Kth 
            else:
                prevLast.next  =Kth

            prevLast = temp
            temp = nextNode

        return head
                

        