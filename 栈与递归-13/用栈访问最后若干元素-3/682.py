class Solution:
    def calPoints(self, ops: List[str]) -> int:
        # res = [0] * len(ops)
        # s = 0
        # p = -1
        # for i in ops:
        #     p += 1
        #     if i == '+':
        #         res[p] = res[p-1] + res[p-2]
        #     elif i == 'D':
        #         res[p] = res[p-1] * 2
        #     elif i == 'C':
        #         res[p-1] = 0
        #         p -= 2
        #     else:
        #         res[p] = int(i)
        # for i in res:
        #     s += i
        # return s

        stack = []
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))

        return sum(stack)