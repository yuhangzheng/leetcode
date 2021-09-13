class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a = b = c = float('-inf')
        d = e = float('inf')
        for num in nums:
            if num > a:
                c = b
                b = a
                a = num
            elif num > b:
                c = b
                b = num
            elif num > c:
                c = num

            if num < e:
                d = e
                e = num
            elif num < d:
                d = num
        return max(a * b * c, a * d * e)


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[-1] * nums[0] * nums[1])