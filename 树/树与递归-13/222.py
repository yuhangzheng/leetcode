# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:

#     def countNodes(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         left = self.countNodes(root.left)
#         right = self.countNodes(root.right)
#         return left + right + 1

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        h = 0
        node = root
        while node:
            h += 1
            node = node.left

        def check(num):
            path = [num]
            while len(path) < h:
                num = (num + 1) // 2
                path.append(num)
            path = path[::-1]
            cur = root
            for i in range(h - 1):
                if path[i + 1] == path[i] * 2:
                    if not cur.right:
                        return False
                    cur = cur.right
                else:
                    if not cur.left:
                        return False
                    cur = cur.left
            return True

        low = 1
        high = 2 ** (h - 1)

        while low < high - 1:
            mid = low + (high - low) // 2
            flag = check(mid)
            if flag:
                low = mid
            else:
                high = mid

        last = high if check(high) else low

        return 2 ** (h - 1) - 1 + last
