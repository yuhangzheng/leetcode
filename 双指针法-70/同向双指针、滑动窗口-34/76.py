class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        解题思路：滑动窗苦即可
        因为t中的字母可以是重复的多个，故用字典来记录处理t中出现的次数比较方便
        '''
        t_dict, window_dict = {}, {}
        for i in range(len(t)):  # 将字符串t进行字典化
            if t[i] in t_dict:
                t_dict[t[i]] += 1
            else:
                t_dict[t[i]] = 1
        for key in t_dict:  # 初始化滑动窗口的字典
            window_dict[key] = 0
        res, start, min_len = '', 0, float('inf')
        for end in range(len(s)):
            if s[end] in window_dict: window_dict[s[end]] += 1
            while self.valid_window(t_dict, window_dict):  # 如果滑动窗口里的字符一直满足即包括t字符串，则满足；需要滑动start寻找最小的
                if min_len > end - start + 1:  # 记录最小的长度，跟长度最小的子串
                    min_len, res = end - start + 1, s[start: end + 1]
                if s[start] in window_dict:  # 在里面就要减一，直到不符合为止，这样才能找到最短的子串
                    window_dict[s[start]] -= 1
                start += 1  # 不管在不在window_dict里，都需要将start+1，这样一直缩小范围，直到不符合
        return res

    def valid_window(self, t_value, win_value):
        for key in t_value:
            if win_value[key] < t_value[key]: return False
        return True
