class Solution:
    def getImportance(self, employees: List['Employee'], idx: int) -> int:
        mp = {employee.id: employee for employee in employees}

        total = 0
        que = collections.deque([idx])
        while que:
            curIdx = que.popleft()
            employee = mp[curIdx]
            total += employee.importance
            for subIdx in employee.subordinates:
                que.append(subIdx)

        return total

