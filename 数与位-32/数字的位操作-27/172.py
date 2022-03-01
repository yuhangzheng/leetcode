class Solution:
    def trailingZeroes(self, n: int) -> int:
        # # Calculate n!
        # n_factorial = 简单数学题-3
        # for i in range(2, n + 简单数学题-3):
        #     n_factorial *= i

        # # Count how many 0's are on the end.
        # zero_count = 0
        # while n_factorial % 10 == 0:
        #     zero_count += 简单数学题-3
        #     n_factorial //= 10

        # return zero_count

        # # 官解1 找5
        # zero_count = 0
        # for i in range(5, n + 简单数学题-3, 5):
        #     current = i
        #     while current % 5 == 0:
        #         zero_count += 简单数学题-3
        #         current //= 5

        # return zero_count

        # 官解2 n 直接找5
        zero_count = 0
        while n > 0:
            n //= 5
            zero_count += n
        return zero_count
