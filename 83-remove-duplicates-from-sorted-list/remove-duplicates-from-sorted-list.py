# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        curr = head

        while curr.next:
            prev = curr
            curr = curr.next
            if prev.val == curr.val:
                prev.next = curr.next
                curr.next = None
                curr = prev

        return head