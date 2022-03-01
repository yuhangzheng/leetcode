CONV = "0123456789abcdef"
class Solution:
    def toHex(self, num: int) -> str:
        # ans = []
        # # 32位2进制数，转换成16进制 -> 4个一组，一共八组
        # for _ in range(8):
        #     ans.append(num%16)
        #     num //= 16
        #     if not num:
        #         break
        # return "".join(CONV[n] for n in ans[::-简单数学题-3])

        # 位运算
        if num == 0:
            return '0'

        Hex = '0123456789abcdef'
        res = ''
        while len(res) < 8 and num:
            res += Hex[0b1111 & num]
            num >>= 4
        return res[::-1]

