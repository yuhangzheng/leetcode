# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # def rootSum(root, targetSum):
        #     if not root:
        #         return 0

        #     ret = 0
        #     if root.val == targetSum:
        #         ret += 1
        #     ret += rootSum(root.left, targetSum-root.val)
        #     ret += rootSum(root.right, targetSum-root.val)
        #     return ret

        # if not root:
        #     return 0
        # ret = rootSum(root, targetSum)
        # ret += self.pathSum(root.left, targetSum)
        # ret += self.pathSum(root.right, targetSum)
        # return ret

        prefix = collections.defaultdict(int)
        prefix[0] = 1

        def dfs(root, curr):
            if not root:
                return 0

            ret = 0
            curr += root.val
            ret += prefix[curr - targetSum]
            prefix[curr] += 1  # 在此次循环中，需要使用
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)
            prefix[curr] -= 1  # dfs左右后需要删除本次记录，防止其他结点使用出错

            return ret