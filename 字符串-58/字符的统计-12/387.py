## 哈希表-26\计数器
class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = collections.Counter(s)
        for i in range(len(s)):
            if frequency[s[i]] == 1:
                return i
        return -1

## 哈希表-26\字典
class Solution:
    def firstUniqChar(self, s: str) -> int:
        position = dict()
        n = len(s)
        for i in range(n):
            if s[i] in position:
                position[s[i]] = -1
            else:
                position[s[i]] = i
        first = n
        for pos in position.values():
            if pos != -1 and pos < first:
                first = pos
        if first == n:
            return -1
        return first

## 队列
class Solution:
    def firstUniqChar(self, s: str) -> int:
        position = dict()
        q = collections.deque()
        n = len(s)
        for i in range(n):
            if s[i] not in position:
                position[s[i]] = i
                q.append((s[i],i))
            else:
                position[s[i]] = -1
                while q and position[q[0][0]] == -1:
                    q.popleft()
        return q[0][1] if q else -1