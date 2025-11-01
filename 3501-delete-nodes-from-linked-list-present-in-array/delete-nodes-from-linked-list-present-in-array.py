# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        st = set(nums) 
        temp = ListNode(0)
        temp.next = head
        curr = temp 

        while curr.next :
            if curr.next.val in st :
                curr.next = curr.next.next

            else:
                curr = curr.next 

        return temp.next

        