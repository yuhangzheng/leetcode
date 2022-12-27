class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        m = 0
        l = 0
        r = n-1
        while l < r:
            if height[l] < height[r]:
                m = max(height[l] * (r-l), m)
                l += 1
            else:
                m = max(height[r] * (r-l), m)
                r -= 1
        return m