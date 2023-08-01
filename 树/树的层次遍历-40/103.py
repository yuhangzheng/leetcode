# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        dq, res, flag = deque(), [], 1
        dq.append(root)
        while len(dq) != 0:
            temp= []
            for i in range(len(dq)):
                node = dq.popleft()
                temp.append(node.val)
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
            if flag == 1:
                res.append(temp[:])
                flag = 0
            else:
                res.append(temp[::-1])
                flag = 1
        return res
