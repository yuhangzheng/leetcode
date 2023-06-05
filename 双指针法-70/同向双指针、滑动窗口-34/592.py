class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 滑动窗口+双指针
        n = len(s)
        if n < 2:
            return n
        left = right = res = maxCount = 0
        freq = [0] * 26
        while right < n:
            freq[ord(s[right])-65] += 1
            maxCount = max(maxCount, freq[ord(s[right])-65])
            right += 1

            if right - left > maxCount + k:
                freq[ord(s[left])-65] -= 1
                left += 1
            res = max(res, right - left)
        return res