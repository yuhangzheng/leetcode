class Solution:
    def frequencySort(self, s: str) -> str:
        li = []
        for i, j in collections.Counter(s).items():
            li.append([i, j])
        new_li = sorted(li, key = lambda x : -x[1])
        return ''.join(i * j for i, j in new_li)