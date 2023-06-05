class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1 = len(s)
        n2 = needNum = len(t)
        if n1 < n2:
            return ""
        left = right = 0
        res=(0,n1 + 1)
        need = collections.Counter(t)
        for right, c in enumerate(s):
            if need[c] > 0:
                needNum -=1
            need[c] -= 1
            if needNum == 0:
                while True:
                    if need[s[left]] == 0:
                        break
                    need[s[left]] += 1
                    left += 1
                if right - left < res[1] - res[0]:
                    res = (left, right)
                need[s[left]] += 1
                needNum += 1
                left += 1
        return '' if res[1] > n1 else s[res[0]:res[1]+1]