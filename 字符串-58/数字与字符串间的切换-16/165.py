class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1, s2 = version1.split('.'), version2.split('.')
        flag = False
        if len(s1) > len(s2):
            flag = True
        n = len(s1)
        if flag:
            n = len(s2)
        for i in range(n):
            i1, i2 = int(s1[i]), int(s2[i])
            if(i1 < i2):
                return -1
            elif(i1 > i2):
                return 1
        if flag:
            for i in range(n, len(s1)):
                if int(s1[i]) > 0:
                    return 1
        else :
            for i in range(n, len(s2)):
                if int(s2[i]) > 0:
                    return -1
        return 0