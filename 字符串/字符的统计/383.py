## 数组移除
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        for word in list(magazine):
            if word in ransomNote:
                ransomNote.remove(word)
        if len(ransomNote) == 0: return True
        else: return False

## 存储字母数
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr = [0] * 26
        for str in magazine:
            arr[ord(str) - ord('a')] += 1
        for str in ransomNote:
            if arr[ord(str) - ord('a')] == 0:
                return False
            else:
                arr[ord(str) - ord('a')] -= 1
        return True

## 哈希\计数器
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_1 = collections.Counter(ransomNote)
        count_2 = collections.Counter(magazine)
        k = 0
        for i, j in count_1.items():
            if i in count_2 and j <= count_2[i]:
                k += 1
        return k == len(count_1)

## 字典\哈希\计数器 优
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h=collections.Counter(magazine)
        for char in ransomNote:
            h[char]-=1
            if h[char]<0:
                return False
        return True
