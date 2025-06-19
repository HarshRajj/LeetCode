"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # This approach uses a hashmap, so taking up extra space of O(n)
        '''
        if not head:
            return None

        
        dic: dict[Node, Node] = {}
        temp = head
        while temp:
            dic[temp] = Node(temp.val)
            temp = temp.next

        
        temp = head
        while temp:
            copied = dic[temp]
            copied.next = dic.get(temp.next)
            copied.random = dic.get(temp.random)
            temp = temp.next

        
        return dic[head]
        '''

        # Now, here is a space optimal approach
        
        if not head:
            return None

        
        temp = head 
        while temp:
            copy_node = Node(temp.val)
            copy_node.next = temp.next 
            temp.next = copy_node 
            temp = copy_node.next

        
        temp = head 
        while temp:
            copy_node = temp.next 
            if temp.random:
                copy_node.random = temp.random.next 
            temp = temp.next.next

        
        dummy = Node(-1)
        res = dummy 
        temp = head
        while temp:
            copy_node = temp.next
            temp.next = copy_node.next  
            res.next = copy_node        
            res = res.next
            temp = temp.next

        return dummy.next


        
