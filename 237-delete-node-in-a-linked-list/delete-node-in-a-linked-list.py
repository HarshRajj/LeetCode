# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        """
        prev = None
        while node.next!= None :
            node.val = node.next.val 
            prev = node
            node = node.next

        del node 
        prev.next = None