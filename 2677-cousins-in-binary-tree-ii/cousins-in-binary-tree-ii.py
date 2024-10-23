# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        lvlq = deque([root])
        sumslist = []
        while lvlq:
            lvlsum = 0
            lvlsize = len(lvlq)
            for _ in range(lvlsize):
                node = lvlq.popleft()
                lvlsum += node.val
                if node.left:
                    lvlq.append(node.left)
                if node.right:
                    lvlq.append(node.right)
            sumslist.append(lvlsum)


        lvlq.append(root)
        lvl = 1
        root.val = 0
        while lvlq:
            lvlsize = len(lvlq)
            for _ in range(lvlsize):
                node = lvlq.popleft()

                sibsum = (node.left.val if node.left else 0
                ) + (node.right.val if node.right else 0)

                if node.left:
                    node.left.val = sumslist[lvl] - sibsum
                    lvlq.append(node.left)
                if node.right:
                    node.right.val = sumslist[lvl] - sibsum
                    lvlq.append(node.right)

            lvl += 1
        return root