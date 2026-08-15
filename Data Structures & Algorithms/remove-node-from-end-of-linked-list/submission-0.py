# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a =[]
        cur = head
         
        while cur:
            a.append(cur)
            cur = cur.next

        l = len(a)
        i = l - n 

        if i ==0:
            return head.next
        
        a[i-1].next = a[i].next
        return head