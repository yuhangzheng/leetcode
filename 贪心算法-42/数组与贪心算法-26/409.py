class Solution:
    def longestPalindrome(self, s: str) -> int:
        # n = len(s)
        # hashmap = {}
        # for st in s:
        #     if st in hashmap:
        #         hashmap[st] += 1
        #     else:
        #         hashmap[st] = 1
        # for key in hashmap:
        #     if hashmap[key] % 2 == 1:
        #         n -= 1

        # return n+1 if n < len(s) else n

        ans = 0
        count = collections.Counter(s)
        for v in count.values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans
