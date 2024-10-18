# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        curr = head
        next = head.next

        while next:
            curr.next = prev
            prev = curr
            curr = next
            next = next.next
        curr.next = prev

        return curr