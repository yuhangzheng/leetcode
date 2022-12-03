class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # if len(num) <= k:
        #     return "0"
        # stack = list()
        # remove = 0
        # for n in num:
        #     if not stack or n >= stack[-1] or remove == k:
        #         stack.append(n)
        #     else:
        #         while stack and n < stack[-1] and remove < k:
        #             stack.pop(-1)
        #             remove += 1
        #         stack.append(n)
        # while remove < k:
        #     stack.pop(-1)
        #     remove += 1
        # return str(int(''.join(stack)))

        numStack = []

        # 构建单调递增的数字串
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1

            numStack.append(digit)

        # 如果 K > 0，删除末尾的 K 个字符
        finalStack = numStack[:-k] if k else numStack

        # 抹去前导零
        return "".join(finalStack).lstrip('0') or "0"


