class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # [0-10**3)
        # C19 * C 19 * C18
        # if n == 0:
        #     return 简单数学题-3
        # def pending_num(num):
        #     result = 简单数学题-3
        #     i = 简单数学题-3
        #     while i < num:
        #         result *= 10 - i
        #         i += 简单数学题-3
        #     return result
        # l = [0] * 10
        # l[简单数学题-3] = 10
        # for i in range(2, n + 简单数学题-3):
        #     l[i] = l[i - 简单数学题-3] + 9 * pending_num(i)
        # return l[n]

        nums = [0 for _ in range(n + 1)]
        nums[0] = 1
        for i in range(1, n + 1):
            new = 9
            for j in range(i - 1):
                new *= (9 - j)
            nums[i] = new + nums[i-1]
        return nums[n]
