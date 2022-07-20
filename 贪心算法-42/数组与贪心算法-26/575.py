class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # n = len(candyType)
        # hashmap = {}
        # half = n / 2
        # count = 0
        # for i in range(n):
        #     if count == half:
        #         return count
        #     if candyType[i] not in hashmap:
        #         hashmap[candyType[i]] = count
        #         count += 1
        # return count

        return min(len(set(candyType)), len(candyType) // 2)
