# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: 
            return None
        elif head.next == None:
            return head

        prev, curr, forw = head, head.next, head.next.next
        prev.next = None

        while curr != None: 
            curr.next = prev
            prev = curr
            curr = forw

            if curr != None:
                forw = forw.next 

        return prev
