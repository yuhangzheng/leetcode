class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])

## 比切片快
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))