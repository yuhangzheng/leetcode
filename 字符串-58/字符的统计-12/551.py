class Solution:
    def checkRecord(self, s: str) -> bool:
        count_a = count_l = 0
        for i in range(len(s)):
            if(s[i] == "A"):
                count_a += 1
                count_l = 0
                if count_a == 2:
                    return False
            elif(s[i] == "L"):
                count_l += 1
                if count_l == 3:
                    return False
            elif(s[i] == "P"):
                count_l = 0
        return True