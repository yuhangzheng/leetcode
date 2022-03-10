# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         word2ch = dict()
#         ch2word = dict()
#         words = s.split()
#         if len(pattern) != len(words):
#             return False

#         for ch, word in zip(pattern, words):
#             if (word in word2ch and word2ch[word] != ch) or (ch in ch2word and ch2word[ch] != word):
#                 return False
#             word2ch[word] = ch
#             ch2word[ch] = word

#         return True
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        pattern = [c for c in pattern]
        if len(s) != len(pattern):
            return False
        mapping = dict()
        for i in range(len(s)):
            c1 = pattern[i]  # c1: pattern  i位置上的字符
            c2 = s[i]  # c2: s        i位置上的字符
            if c1 not in mapping:
                if c2 in mapping.values():  # 相同c2只能匹配一次
                    return False
                mapping[c1] = c2
            else:
                if mapping[c1] != c2:
                    return False
        return True
