# class Solution:
#     def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # 超时
#         n = len(s)
#         if n < 10:
#             return []
#         res = []
#         for p in range(n-10):
#             for q in range(p+1, n-9):
#                 i = 0
#                 while i < 10 and s[p+i] == s[q+i]:
#                     i += 1
#                 if i == 10:
#                     res.append(s[p:p+10])
#         return list(set(res))
L = 10
# 哈希表
# class Solution:
#     def findRepeatedDnaSequences(self, s: str) -> List[str]:
#         ans = []
#         cnt = defaultdict(int)
#         for i in range(len(s) - L + 1):
#             sub = s[i : i + L]
#             cnt[sub] += 1
#             if cnt[sub] == 2:
#                 ans.append(sub)
#         return ans

# 编码哈希
L = 10
bin = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= L:
            return []
        ans = []
        x = 0
        for ch in s[:L - 1]:
            x = (x << 2) | bin[ch]
        cnt = defaultdict(int)
        for i in range(n - L + 1):
            x = ((x << 2) | bin[s[i + L - 1]]) & ((1 << (L * 2)) - 1)
            cnt[x] += 1
            if cnt[x] == 2:
                ans.append(s[i : i + L])
        return ans
