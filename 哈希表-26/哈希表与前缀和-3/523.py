class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # d = {0: -1}
        # pre = 0
        # for index, num in enumerate(nums):
        #     pre += num
        #     rem = pre % k
        #     i = d.get(rem, index)
        #     if i == index:
        #         d[rem] = index
        #     elif i <= index - 2:
        #         return True
        # return False

        # 同余定理
        modes = set()
        presum = 0
        for num in nums:
            last = presum
            # 当前前缀和
            presum += num
            presum %= k
            # 同余定理
            if presum in modes:
                return True
            # 上一个前缀和，下一个就可以用了（距离为2了）
            modes.add(last)
        return False
