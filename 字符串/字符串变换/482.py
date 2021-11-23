class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = list()
        cnt = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] != "-":
                ans.append(s[i].upper())
                cnt += 1
                if cnt % k == 0:
                    ans.append("-")

        if ans and ans[-1] == "-":
            ans = ans[:len(ans) - 1]

        return "".join(ans[::-1])