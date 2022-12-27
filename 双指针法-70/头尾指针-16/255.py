class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        lMax = rMax = 0
        l = 0
        r = len(height) - 1
        while l < r:
            lMax = max(height[l], lMax)
            rMax = max(height[r], rMax)
            if height[l] < height[r]:
                res += lMax - height[l]
                l += 1
            else:
                res += rMax - height[r]
                r -= 1
        return res

# 动规
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height:
#             return 0

#         n = len(height)
#         leftMax = [height[0]] + [0] * (n - 1)
#         for i in range(1, n):
#             leftMax[i] = max(leftMax[i - 1], height[i])

#         rightMax = [0] * (n - 1) + [height[n - 1]]
#         for i in range(n - 2, -1, -1):
#             rightMax[i] = max(rightMax[i + 1], height[i])

#         ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
#         return ans

# 单调栈
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         ans = 0
#         stack = list()
#         n = len(height)

#         for i, h in enumerate(height):
#             while stack and h > height[stack[-1]]:
#                 top = stack.pop()
#                 if not stack:
#                     break
#                 left = stack[-1]
#                 currWidth = i - left - 1
#                 currHeight = min(height[left], height[i]) - height[top]
#                 ans += currWidth * currHeight
#             stack.append(i)

#         return ans
