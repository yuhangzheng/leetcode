class Solution:
    def bulbSwitch(self, n: int) -> int:
        # 超时
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # temp = [1] * n
        # for i in range(2, n+1):
        #     print(i)
        #     for j in range(i-1, n, i):
        #         # print(j)
        #         temp[j-1] = -temp[j-1]
        #         # print(temp)
        # return temp.count(1)

        # 官解
        # 对于 k，约数都是「成对」出现的。这就说明，只有当 kk 是「完全平方数」时，它才会有奇数个约数，否则一定有偶数个约数。
        # 因此我们只需要找出完全平方数的个数即可，由于涉及到浮点数运算，为了保证不出现精度问题，我们可以计算 sqrt(n+1/2)
        # 这样可以保证计算出来的结果向下取整在 3232 位整数范围内一定正确。

        return int(sqrt(n + 0.5))
