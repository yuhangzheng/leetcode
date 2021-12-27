class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # str1 = bin(n)
        # for i in range(len(str1)-1):
        #     if str1[i] == str1[i+1]:
        #         return False
        # return True
        flag = n & 1
        n = n >> 1
        while n > 0:
            if flag == n & 1:
                return False
            flag = n & 1
            n = n >> 1
        return True
