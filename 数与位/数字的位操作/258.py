class Solution:
    def addDigits(self, num: int) -> int:
        # temp = num
        # while temp >= 10:
        #     temp = 0
        #     while num > 0:
        #         temp += num % 10
        #         num = num //10
        #     num = temp
        # return num
        # 数学法
        if (num % 9 == 0) and (num != 0):
            return 9
        else:
            return num % 9
