class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_sort = sorted(score, reverse=True)
        rank_list = ["Gold Medal", "Silver Medal",
                     "Bronze Medal"]+[str(i+4) for i in range(len(score)-3)]
        ## 字典 和zip 语法糖
        dic = dict(zip(score_sort, rank_list))
        res = [dic.get(i) for i in score]
        return res
