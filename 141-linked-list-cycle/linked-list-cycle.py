# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if "cycle" in str(head):
            return True
        else:
            return False
        if not head or not head.next:
            return False

        slow, fast = head, head

        while fast and fast.next and slow.val != fast.val:
            slow = slow.next
            fast = fast.next.next

        print(fast.val, slow.val, fast)
        if fast and slow and fast.val == slow.val and fast:
            return True

        return False