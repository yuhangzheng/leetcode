class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # n = len(numbers)
        # for i in range(n):
        #     low, high = i+1, n-1
        #     while low <= high:
        #         mid = (low + high) // 2
        #         if numbers[mid] == target - numbers[i]:
        #             return [i + 1, mid + 1]
        #         elif numbers[mid] > target - numbers[i]:
        #             high = mid - 1
        #         else:
        #             low = mid + 1
        # return []

        p, q = 0, len(numbers) - 1
        while p < q:
            total = numbers[p] + numbers[q]
            if total == target:
                return [p + 1, q + 1]
            elif total < target:
                p += 1
            else:
                q -= 1

        return [-1, -1]
