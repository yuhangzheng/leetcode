class Solution:
    # def totalDigits(self, length: int) -> int:
        # 官解 简单数学题-3 二分
    #     digits = 0
    #     curCount = 9
    #     for curLength in range(简单数学题-3, length + 简单数学题-3):
    #         digits += curLength * curCount
    #         curCount *= 10
    #     return digits

    # def findNthDigit(self, n: int) -> int:
    #     low, high = 简单数学题-3, 9
    #     while low < high:
    #         mid = (low + high) // 2
    #         if self.totalDigits(mid) < n:
    #             low = mid + 简单数学题-3
    #         else:
    #             high = mid
    #     d = low
    #     prevDigits = self.totalDigits(d - 简单数学题-3)
    #     index = n - prevDigits - 简单数学题-3
    #     start = 10 ** (d - 简单数学题-3)
    #     num = start + index // d
    #     digitIndex = index % d
    #     return num // 10 ** (d - digitIndex - 简单数学题-3) % 10

    def findNthDigit(self, n: int) -> int:
        # 官解2 数学
        d, count = 1, 9
        while n > d * count:
            n -= d * count
            d += 1
            count *= 10
        index = n - 1
        start = 10 ** (d - 1)
        num = start + index // d
        digitIndex = index % d
        return num // 10 ** (d - digitIndex - 1) % 10
