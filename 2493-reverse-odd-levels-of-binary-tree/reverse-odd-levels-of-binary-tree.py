# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = 0
        if not root:
            return root

        q = deque([root])

        while q:
            size = len(q)
            l = 0
            r = len(q) - 1

            if level % 2 == 1:
                while l < r:
                    q[l].val, q[r].val = q[r].val, q[l].val
                    r -= 2
                    size -= 1
                    if q[l].left:
                        q.append(q[l].left)
                    
                    if q[l].right:
                        q.append(q[l].right)
                    
                    q.popleft()

            while l < size:
                if q[l].left:
                    q.append(q[l].left)
                
                if q[l].right:
                    q.append(q[l].right)
                
                q.popleft()
                size -= 1
            level += 1

        return root