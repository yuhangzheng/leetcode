class Solution: ## 错误 “IV”
    def romanToInt(self, s: str) -> int:
        sum = 0
        for i in range(len(s)):
            if s[i] == 'I' and i < len(s) - 1:
                if s[i + 1] == 'V':
                    sum += 4
                    i += 1
                else:
                    sum += 1
            elif s[i] == 'I' and i < len(s) - 1:
                if s[i + 1] == 'X':
                    sum += 9
                    i += 1
                else:
                    sum += 1
            elif s[i] == 'X' and i < len(s) - 1:
                if s[i + 1] == 'L':
                    sum += 50
                    i += 1
                else:
                    sum += 10
            elif s[i] == 'X' and i < len(s) - 1:
                if s[i + 1] == 'C':
                    sum += 90
                    i += 1
                else:
                    sum += 10
            elif s[i] == 'C' and i < len(s) - 1:
                if s[i + 1] == 'D':
                    sum += 500
                    i += 1
                else:
                    sum += 100
            elif s[i] == 'C' and i < len(s) - 1:
                if s[i + 1] == 'M':
                    sum += 1000
                    i += 1
                else:
                    sum += 100
            elif s[i] == 'I':
                sum += 1
            elif s[i] == 'V':
                sum += 5
            elif s[i] == 'X':
                sum += 10
            elif s[i] == 'L':
                sum += 50
            elif s[i] == 'C':
                sum += 100
            elif s[i] == 'D':
                sum += 500
            elif s[i] == 'M':
                sum += 1000
            print(sum)
        return sum

class Solution:

    SYMBOL_VALUES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i, ch in enumerate(s):
            value = Solution.SYMBOL_VALUES[ch]
            if i < n - 1 and value < Solution.SYMBOL_VALUES[s[i + 1]]:  ## 精髓
                ans -= value
            else:
                ans += value
        return ans