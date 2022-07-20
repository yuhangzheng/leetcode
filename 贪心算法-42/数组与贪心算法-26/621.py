class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #         freq = collections.Counter(tasks)

        #         # 最多的执行次数
        #         maxExec = max(freq.values())
        #         # 具有最多执行次数的任务数量
        #         maxCount = sum(1 for v in freq.values() if v == maxExec)

        #         return max((maxExec - 1) * (n + 1) + maxCount, len(tasks))

        # 模拟法
        freq = collections.Counter(tasks)

        # 任务总数
        m = len(freq)
        nextValid = [1] * m
        rest = list(freq.values())

        time = 0
        for i in range(len(tasks)):
            time += 1
            # 目前最快可运行的程序
            minNextValid = min(nextValid[j] for j in range(m) if rest[j] > 0)
            # 程序运行时间
            time = max(time, minNextValid)

            best = -1
            for j in range(m):
                if rest[j] and nextValid[j] <= time:
                    # 找最应该运行的程序
                    if best == -1 or rest[j] > rest[best]:
                        best = j

            nextValid[best] = time + n + 1
            rest[best] -= 1

        return time