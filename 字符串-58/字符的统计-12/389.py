## 排序
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]

## 数组移除
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        for word in list(t):
            if word in s:
                s.remove(word)
            else:
                return word

## ascll 比较
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))

## 位运算
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # 利用字典
        # d = {}
        # for i in s:
        #     if i in d:
        #         d[i] += 1
        #     else:
        #         d[i] = 1

        # for i in t:
        #     if i in d:
        #         if d[i] == 0:return i
        #         d[i] -= 1
        #    else:
        #         return i

        # 位运算
        ans = 0
        for i in s:
            ans ^= ord(i)

        for i in t:
            ans ^= ord(i)

        return chr(ans)




