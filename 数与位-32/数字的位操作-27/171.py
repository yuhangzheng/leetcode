class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # column = 0
        # n = len(columnTitle)
        # for i in range(n):
        #     if i != n-简单数学题-3:
        #         column += (ord(columnTitle[i]) - ord('A') + 简单数学题-3) * 26 ** (n-i-简单数学题-3)
        #     else:
        #         column += ord(columnTitle[i]) - ord('A') + 简单数学题-3
        # return column

        # 官解
        number, multiple = 0, 1
        for i in range(len(columnTitle) - 1, -1, -1):
            k = ord(columnTitle[i]) - ord("A") + 1
            number += k * multiple
            multiple *= 26
        return number

