class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # m = len(nums1)
        # n = len(nums2)
        # ans = [-1] * m
        # for i in range(m):
        #     k = -1
        #     for j in range(n):
        #         if nums1[i] == nums2[j]:
        #             k = j
        #     while k < n:
        #         if nums2[k] > nums1[i]:
        #             ans[i] = nums2[k]
        #             break
        #         else:
        #             k += 1
        # return ans

        # 单调栈
        res = {}
        stack = []
        for num in reversed(nums2):
            while stack and num >= stack[-1]:
                stack.pop()
            res[num] = stack[-1] if stack else -1
            stack.append(num)
        return [res[num] for num in nums1]