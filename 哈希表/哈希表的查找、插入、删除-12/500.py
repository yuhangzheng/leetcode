class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # ans = []
        # rowIdx = "12210111011122000010020202"
        # for word in words:
        #     idx = rowIdx[ord(word[0].lower()) - ord('a')]
        #     if all(rowIdx[ord(ch.lower()) - ord('a')] == idx for ch in word):
        #         ans.append(word)
        # return ans

        LINES = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]

        m = []
        for word in words:
            if any(set(word.lower()).issubset(line) for line in LINES) == True:
                m.append(word)
        return m
