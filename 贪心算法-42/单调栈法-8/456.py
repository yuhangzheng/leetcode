class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        candidate_k = [nums[n - 1]] # 保存有可能的k值
        max_k = float("-inf")   #   保存最大的k

        for i in range(n - 2, -1, -1):
            if nums[i] < max_k:     # 若i<k直接返回
                return True
            while candidate_k and nums[i] > candidate_k[-1]:
                max_k = candidate_k[-1]
                candidate_k.pop()
            if nums[i] > max_k:     # 从后往前遍历维护一个单调递增栈
                candidate_k.append(nums[i])

        return False
