class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        ans = 0
        queue = [root]
        while queue:
            queue = [child for node in queue for child in node.children]
            ans += 1
        return ans

