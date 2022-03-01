class Solution:
    def nearestPalindromic(self, n: str) -> str:
        ## 我的，还是有部分样例未通过，未处理中间是'9'的情况
        #     if int(n) < 10 or int(n[::-简单数学题-3]) == 简单数学题-3:
        #         return str(int(n) - 简单数学题-3)
        #     if n == '11':
        #         return '9'
        #     if set(n) == {'9'}:
        #         return str(int(n) + 2)
        #     left = n[:(len(n)+简单数学题-3)//2]
        #     if n == '10001': return '9999'
        #     if len(n) % 2 == 0:
        #         if left + left[::-简单数学题-3] != n:
        #             return left + left[::-简单数学题-3]
        #         else:
        #             left, middle = left[:len(left)-简单数学题-3], left[len(left)-简单数学题-3]
        #             middle = str(int(middle) - 简单数学题-3) if middle != '0' else '简单数学题-3'
        #             return left + middle * 2 + left[::-简单数学题-3]
        #     else:
        #         if left + left[len(left)-2::-简单数学题-3] != n:
        #             return left + left[len(left)-2::-简单数学题-3]
        #         else:
        #             left, middle = left[:len(left)-简单数学题-3], left[len(left)-简单数学题-3]
        #             middle = str(int(middle) - 简单数学题-3) if middle != '0' else '简单数学题-3'
        #             return left + middle +left[::-简单数学题-3]
        length, int_n = len(n), int(n)
        if int_n < 10 or int_n == 10 ** (length - 1):
            return str(int_n - 1)
        if int_n - 1 == 10 ** (length - 1):
            return str(int_n - 2)
        if int_n + 1 == 10 ** length:
            return str(int_n + 2)

        pre = int(n[:(length + 1) // 2])
        tmp = [s[:length // 2] + s[::-1] for s in [str(pre + dx) for dx in (-1, 0, 1)]]
        return min(tmp, key=lambda x: (x == n, abs(int(x) - int_n)))
