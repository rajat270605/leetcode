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
        if not head:
            return None 
        c = head
        while c:
            next_node = c.next
            copy = Node(c.val)

            c.next = copy
            copy.next = next_node

            c = c.next.next
        
        c = head
        while c:
            copy = c.next
            copy.random = c.random.next if c.random else None
            c = c.next.next
        
        c = head
        copy_head = c.next

        while c:
            copy = c.next
            c.next = c.next.next
            copy.next = c.next.next if c.next else None 

            c = c.next
        return copy_head

        
