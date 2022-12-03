class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        # 设置队列来模拟投票
        radiant = collections.deque()
        dire = collections.deque()
        for i, s in enumerate(senate):
            if s == "R":
                radiant.append(i)
            else:
                dire.append(i)
        # 开始投票
        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0]+n)
            else:
                dire.append(dire[0]+n)
            radiant.popleft()
            dire.popleft()
        return "Radiant" if radiant else "Dire"