# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque()
        sums = []
        q.append(root)
        level = 0

        while q:
            csum = 0
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                csum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                
            heapq.heappush(sums, -csum)
            level += 1

        if level < k:
            return -1
        final = 0
        for _ in range(k):
            final = heapq.heappop(sums)

        return -final