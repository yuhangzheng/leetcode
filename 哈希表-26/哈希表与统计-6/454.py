class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # # 分为 A+B  C+D 两组
        # countAB = collections.Counter(u + v for u in nums1 for v in nums2)
        # countCD = collections.Counter(-u - v for u in nums3 for v in nums4)
        # count = 0
        # for key in countAB:
        #     if key in countCD:
        #         count += countAB[key] * countCD[key]
        # return count

        countAB = collections.Counter((a + b) for a in nums1 for b in nums2)
        res = 0
        for c in nums3:
            for d in nums4:
                if -c - d in countAB:
                    res += countAB[-c - d]
        return res