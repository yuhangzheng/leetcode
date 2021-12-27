class Solution:
    def trailingZeroes(self, n: int) -> int:
        # # Calculate n!
        # n_factorial = 1
        # for i in range(2, n + 1):
        #     n_factorial *= i

        # # Count how many 0's are on the end.
        # zero_count = 0
        # while n_factorial % 10 == 0:
        #     zero_count += 1
        #     n_factorial //= 10

        # return zero_count

        # # 官解1 找5
        # zero_count = 0
        # for i in range(5, n + 1, 5):
        #     current = i
        #     while current % 5 == 0:
        #         zero_count += 1
        #         current //= 5

        # return zero_count

        # 官解2 n 直接找5
        zero_count = 0
        while n > 0:
            n //= 5
            zero_count += n
        return zero_count
