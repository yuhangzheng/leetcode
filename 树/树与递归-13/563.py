# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        suml = self.dfs(root.left)
        sumr = self.dfs(root.right)
        self.ans += abs(suml - sumr)
        return suml + sumr + root.val

    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.ans