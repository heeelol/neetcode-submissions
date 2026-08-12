# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = temp = ListNode()

        while list1 is not None or list2 is not None:
            if list1 is None:
                temp.next = list2
                break
            elif list2 is None: 
                temp.next = list1
                break
            elif list1.val <= list2.val:
                 temp.next = temp = list1
                 list1 = list1.next
            else:
                temp.next = temp = list2 
                list2 = list2.next

        return node.next 