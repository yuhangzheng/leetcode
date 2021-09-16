class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        #滚动数组
        ret = [1] * (rowIndex + 1)
        for i in range(1,rowIndex+1):
            for j in range(i, 0, -1):
                if j == 0 or j == i :
                    ret[j] = 1
                else:
                    ret[j] = ret[j-1]+ret[j]
        return ret