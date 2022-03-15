# class Solution:
#     def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
#         dic = dict()
#         min = len(list1) + len(list2)
#         ret = []
#         for i in range(len(list1)):
#             if list1[i] not in dic:
#                 dic[list1[i]] = i
#         for i in range(len(list2)):
#             if list2[i] in dic:
#                 if i + dic.get(list2[i]) < min:
#                     ret = []
#                     min = i + dic.get(list2[i])
#                     ret.append(list2[i])
#                 elif i + dic.get(list2[i]) == min:
#                     ret.append(list2[i])
#         return ret

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index = {s: i for i, s in enumerate(list1)}
        ans = []
        indexSum = inf
        for i, s in enumerate(list2):
            if s in index:
                j = index[s]
                if i + j < indexSum:
                    indexSum = i + j
                    ans = [s]
                elif i + j == indexSum:
                    ans.append(s)
        return ans