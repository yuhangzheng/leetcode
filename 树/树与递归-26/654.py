# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        maxNum = -1
        mid = 0
        for i in range(len(nums)):
            if nums[i] > maxNum:
                maxNum = nums[i]
                mid = i

        root = TreeNode(maxNum)
        root.left = self.constructMaximumBinaryTree(nums[:mid])
        root.right = self.constructMaximumBinaryTree(nums[mid + 1:])
        return root