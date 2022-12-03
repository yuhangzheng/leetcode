class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 哈希表加单调栈
        count = Counter(s)
        stack = list()
        for c in s:
            if c not in stack:
                while stack and c < stack[-1] and count[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            count[c] -= 1
        return ''.join(stack)
