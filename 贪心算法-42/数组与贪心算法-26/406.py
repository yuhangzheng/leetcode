class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # people.sort(key=lambda x : (x[0], -x[1]))
        # n = len(people)
        # ans = [[] for _ in range(n)]
        # for person in people:
        #     # 应该放在第几个位置
        #     spaces = person[1] + 1
        #     # 遍历结果数组查找空位
        #     for i in range(n):
        #         if not ans[i]:
        #             spaces -= 1
        #             if spaces == 0:
        #                 ans[i] = person
        # return ans

        # # 从高到低排
        # people.sort(key=lambda x: (-x[0], x[1]))
        # n = len(people)
        # ans = list()
        # for person in people:
        #     ans[person[1]:person[1]] = [person]
        # return ans

        # 贪心
        res = []
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        for p in people:
            if len(res) <= p[1]:
                res.append(p)
            elif len(res) > p[1]:
                res.insert(p[1], p)
        return res
