class Solution: ## 普通
    def myAtoi(self, str: str) -> int:
        i=0
        n=len(str)
        while i<n and str[i]==' ':
            i=i+1
        if n==0 or i==n:
            return 0
        flag=1
        if str[i]=='-':
            flag=-1
        if str[i]=='+' or str[i]=='-':
            i=i+1
        INT_MAX=2**31-1
        INT_MIN=-2**31
        ans=0
        while i<n and '0'<=str[i]<='9':
            ans=ans*10+int(str[i])-int('0')
            i+=1
            if(ans-1>INT_MAX):
                break

        ans=ans*flag
        if ans>INT_MAX:
            return INT_MAX
        return INT_MIN if ans<INT_MIN else ans

class Solution: ## 正则
    def myAtoi(self, str: str) -> int:
        import re
        mathes=re.match('[ ]*([+-]?\d+)',str)
        if not mathes:
            return 0
        ans=int(mathes.group(1))
        return min(max(ans,-2**31),2**31-1)
