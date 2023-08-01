# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        # left = self.invertTree(root.left)
        # right = self.invertTree(root.right)
        # root.left, root.right = right, left
        # return root

        queue = [root]
        while queue:
            t = queue.pop()
            t.left, t. right = t.right, t.left
            if t.left:
                queue.append(t.left)
            if t.right:
                queue.append(t.right)
        return root