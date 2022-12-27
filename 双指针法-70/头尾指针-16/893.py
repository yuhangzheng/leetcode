class Solution:
    def validPalindrome(self, s: str) -> bool:
        # p, q = 0, len(s)-1
        # chance = 1
        # while p < q:
        #     if s[p] == s[q]:
        #         p += 1
        #         q -= 1
        #     else:
        #         if chance == 0:
        #             return False
        #         else:
        #             if s[p] == s[q-1]:
        #                 q -= 1
        #             elif s[p+1] == s[q]:
        #                 p += 1
        #             else:
        #                 return False
        # return True

        def checkPalindrome(low, high):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return checkPalindrome(low + 1, high) or checkPalindrome(low, high - 1)
        return True
