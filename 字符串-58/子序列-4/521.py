class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return -1 if a == b else max(len(a), len(b))