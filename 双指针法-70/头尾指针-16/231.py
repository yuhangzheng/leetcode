class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        if not nums or n < 4:
            return ans

        nums.sort()
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                    continue

                k, l = j + 1, n - 1
                while k < l:
                    sum4 = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum4 == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        k += 1
                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1
                        l -= 1
                    elif sum4 < target:  # 这里用elif 防止下面的else出错
                        k += 1
                    else:
                        l -= 1
        return ans