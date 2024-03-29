# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         #左子树的左孩子==右子树的右孩子 and 左子树的右孩子 == 右子树的左孩子
#         '''
#         递归,自定义函数
#         '''
#         if root is None:
#             return True
#         return self.check(root.left,root.right)

#     def check(self,left: TreeNode,right: TreeNode) -> bool:
#         #递归的终止条件是两个节点都为空
#         #或左右有任意一个不为空，一定不对称
#         #两个节点的值不相等
#         if left is None and right is None:
#             return True
#         if left is None or right is None:
#             return False
#         if left.val != right.val:
#             return False

#         return self.check(left.left,right.right) and self.check(left.right,right.left)

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or (not root.left and not root.right):
            return True

        q = [(root.left, root.right)]
        while q:
            l, r = q.pop()
            if not l and not r:
                continue
            elif not l or not r:
                return False
            if l.val != r.val:
                return False

            q.append((l.left, r.right))
            q.append((l.right, r.left))
        return True
