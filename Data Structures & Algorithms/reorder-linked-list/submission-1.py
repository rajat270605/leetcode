# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = head
        f = head.next 
        while f and f.next:
            s = s.next
            f = f.next.next

        second = s.next
        s.next = None 

        c = second 
        p = None 
        while c:
            n = c.next
            c.next = p
            p = c
            c = n
        
        l1 = head
        l2 = p
        while l2:
            t1 = l1.next
            t2 = l2.next
            l1.next = l2
            l2.next = t1
            l1 = t1
            l2 = t2


        