## 哈希 计数器 优
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_1 = collections.Counter(s)
        count_2 = collections.Counter(t)
        if len(count_1) != len(count_2):
            return False
        for str, fre in count_1.items():
            if str not in count_2 or fre != count_2[str]:
                return False
        return True

##计数器、字典
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

## 统计字母数
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 26
        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')] += 1
        for j in range(len(t)):
            arr[ord(t[j]) - ord('a')] -= 1
        for k in range(26):
            if arr[k] != 0:
                return False
        else:
            return True

## 排序
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l_s = list(s)
        l_s.sort()
        l_t = list(t)
        l_t.sort()
        return l_s == l_t
