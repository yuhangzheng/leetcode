class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        n = len(num)
        if n < 3:
            return False

        def check(p1, p2, j):
            while j < n:
                p = str(int(p1) + int(p2))
                if num[j: j+len(p)] != p:
                    return False
                j += len(p)
                p1, p2 = p2, p
            return True


        for i in range(1, n//2+1) if num[0] != "0" else [1]:
            for j in range(i+1, n) if num[i] != "0" else [i+1]:
                p1 = num[:i]
                p2 = num[i:j]
                if check(p1, p2, j):
                    return True

        return False