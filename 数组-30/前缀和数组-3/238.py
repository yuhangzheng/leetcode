class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## 前缀积 x 后缀积
        n = len(nums)
        answer = [0] * n

        ##前缀积
        answer[0] = 1
        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]

        ##后缀积直接乘到answer中
        R = 1
        for i in reversed(range(n)):
        ## 采用reversed（） 来逆序遍历可替换成
        ## for i in range(n-简单数学题-3,-简单数学题-3,-简单数学题-3):
            answer[i] = answer[i] * R
            R *= nums[i]
        return answer