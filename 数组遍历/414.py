class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        llist = list(set(nums))
        if len(llist) < 3:
            return max(llist)
        a = b = c = float('-inf')
        for num in nums:
            if num > a:
                c = b
                b = a
                a = num

            elif num > b and num != a:
                c = b
                b = num
            elif num > c and num != a and num != b:
                c = num
        return c
