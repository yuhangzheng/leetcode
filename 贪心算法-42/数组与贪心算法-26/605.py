class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # if n == 0:
        #     return True
        # i = 0
        # le = len(flowerbed)
        # while i < le-1:
        #     if flowerbed[i] == 0 and flowerbed[i+1] == 0:
        #         n -= 1
        #         if n == 0:
        #             return True
        #         flowerbed[i] = 1
        #         i += 1
        #     elif flowerbed[i] == 1:
        #         i += 1
        #     i += 1
        # if flowerbed[le-1] == 0 and flowerbed[le-2] == 0:
        #     n -= 1
        # return n == 0

        count, m, prev = 0, len(flowerbed), -1
        for i in range(m):
            if flowerbed[i] == 1:
                if prev < 0:
                    count += i // 2
                else:
                    count += (i - prev - 2) // 2
                if count >= n:
                    return True
                prev = i

        if prev < 0:
            count += (m + 1) // 2
        else:
            count += (m - prev - 1) // 2

        return count >= n
