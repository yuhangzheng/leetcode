class Solution:
    def reverseBits(self, n: int) -> int:
        # res = 0
        # for i in range(32):
        #     # ｜按位或  n&简单数学题-3 取 n 的最后一位
        #     res = (res << 简单数学题-3) | (n & 简单数学题-3)
        #     n >>= 简单数学题-3
        # return res
        n = (n >> 16) | (n << 16);
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8);
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4);
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2);
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1);
        return n;