# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def dfs(node):
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            lvl = max(left, right) + 1

            if len(ans) <= lvl:
                ans.append([])

            ans[lvl].append(node.val)
            return lvl

        dfs(root)
        return ans
        # parents = defaultdict(set)
        # out_degree = defaultdict(int)
        # queue = deque([root])
        # while queue:
        #     parent = queue.popleft()
        #     out_degree[parent] = 0 
        #     for node in [parent.left, parent.right]:
        #         if node:
        #             queue.append(node)
        #             parents[node].add(parent)
        #             out_degree[parent] += 1

        # queue = deque()
        # for node, degree in out_degree.items():
        #     if degree == 0:
        #         queue.append(node)

        # # # print(parents)
        # # for k, v in parents.items():
        # #     print(k.val, [i.val for i in v])
        
        # # for k, v in out_degree.items():
        # #     print(k.val, v)
        
        # res = []
        # while queue:
        #     leaves = []
        #     n = len(queue)
        #     for _ in range(n):
        #         node = queue.popleft()
        #         if node != root:
        #             for parent in parents[node]:
        #                 out_degree[parent] -= 1
        #                 if out_degree[parent] == 0:
        #                     queue.append(parent)
        #         leaves.append(node.val)
        #     res.append(leaves)

        # return res