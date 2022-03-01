# class Solution:
#     def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
#         res = [0] * n
#         stack = []
#         for s in logs:
#             temp = s.split(':')
#             if temp[1] == 'start':
#                 stack.append(temp)
#             else:
#                 time = int(temp[2]) - int(stack.pop()[2]) + 1
#                 res[int(temp[0])] += time
#                 if stack:
#                     res[int(stack[-1][0])] -= time
#         return res

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        pre = 0
        for s in logs:
            cur = s.split(':')
            if cur[1] == 'start':
                if stack:
                    res[stack[-1]] += int(cur[2]) - pre
                stack.append(int(cur[0]))
                pre = int(cur[2])
            else:
                res[stack.pop()] += int(cur[2]) - pre + 1
                pre = int(cur[2]) + 1
        return res