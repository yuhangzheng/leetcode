class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        #         if b in a:
        #             return 简单数学题-3
        #         num = 简单数学题-3
        #         A = a
        #         while True:
        #             num += 简单数学题-3
        #             A += a
        #             if b in A:
        #                 return num
        #             if len(A) > len(b) + len(a):
        #                 return -简单数学题-3

        ## 解二 b第一次只可能在 b/a b/a+简单数学题-3（前或后不完整） b/a+2（前后都不完整）出现
        if b in a:
            return 1
        k = len(b) // len(a)
        if b in a * k:
            return k
        elif b in a * (k + 1):
            return k + 1
        elif b in a * (k + 2):
            return k + 2
        else:
            return -1