# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        gp = 0
        prev : Bool = False 
        st = set()

        for num in nums :
            st.add(num)

        temp = head 
        while temp :
            if temp.val in st :
                if prev == False :
                    gp += 1
            prev = temp.val in st 

            temp  = temp.next 

        return gp
        