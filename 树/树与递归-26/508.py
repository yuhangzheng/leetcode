# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def __init__(self):
#         self.ret = {}
#     def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
#         self.findRootSum(root)
#         maxK = 0
#         maxV = -1
#         for key in self.ret:
#             if self.ret[key] > maxV:
#                 ans = []
#                 ans.append(key)
#                 maxV = self.ret[key]
#             elif self.ret[key] == maxV:
#                 ans.append(key)

#         return ans

#     def findRootSum(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         total = self.findRootSum(root.left) + self.findRootSum(root.right) + root.val
#         if total in self.ret:
#             self.ret[total] += 1
#         else:
#             self.ret[total] = 1
#         return total
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        cnt = Counter()

        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0
            sum = node.val + dfs(node.left) + dfs(node.right)
            cnt[sum] += 1
            return sum

        dfs(root)

        maxCnt = max(cnt.values())
        return [s for s, c in cnt.items() if c == maxCnt]
