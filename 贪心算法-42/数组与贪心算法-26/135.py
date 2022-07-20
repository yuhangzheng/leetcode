class Solution:
    def candy(self, ratings: List[int]) -> int:
        # n = len(ratings)
        # left = [1] * n
        # right = count = 0
        # for i in range(n):
        #     if i > 0 and ratings[i] > ratings[i-1]:
        #         left[i] = left[i-1] + 1

        # for i in range(n-1, -1 ,-1):
        #     if i < n-1 and ratings[i] > ratings[i+1]:
        #         right += 1
        #     else:
        #         right = 1
        #     count += max(left[i], right)
        # return count

        n = len(ratings)
        ret = 1
        inc, dec, pre = 1, 0, 1

        for i in range(1, n):
            if ratings[i] >= ratings[i - 1]:
                dec = 0
                pre = (1 if ratings[i] == ratings[i - 1] else pre + 1)
                ret += pre
                inc = pre
            else:
                dec += 1
                if dec == inc:
                    dec += 1
                ret += dec
                pre = 1

        return ret
