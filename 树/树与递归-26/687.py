# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left1 = left + 1 if node.left and node.left.val == node.val else 0
            right1 = right + 1 if node.right and node.right.val == node.val else 0
            nonlocal ans
            ans = max(ans, left1 + right1)
            return max(left1, right1)

        dfs(root)
        return ans
