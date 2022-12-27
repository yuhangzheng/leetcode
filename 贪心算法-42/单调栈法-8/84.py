class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # if len(heights) == 1:
        #     return heights[0]
        # stack1 = [heights[0]]     # 单增
        # stack2 = [heights[0]]     # 单减
        # ans = len(heights)

        # for i in range(1, len(heights)):
        #     if heights[i] >= stack1[-1]:
        #         stack1.append(heights[i])
        #     else:
        #         stack1 = [heights[i]]
        #     if heights[i] <= stack2[-1]:
        #         stack2.append(heights[i])
        #     else:
        #         stack2 = [heights[i]]
        #     m1 = m2 = 0
        #     for i in range(len(stack1)):
        #         m1 = max(m1, (len(stack1)-i) * stack1[i])
        #     for i in range(len(stack2)):
        #         m2 = max(m2, (i+1) * stack2[i])
        #     ans = max(m1, m2, ans)
        # return ans

        n = len(heights)
        left, right = [0] * n, [0] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        mono_stack = list()
        for i in range(n - 1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans