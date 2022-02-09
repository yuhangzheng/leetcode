class Solution:
    def maximumSwap(self, num: int) -> int:
        # 哈希表
        # num = list(str(num))
        # n = len(num)
        # from collections import Counter
        # dic = collections.Counter(num)
        # for i in range(n):
        #     item = max(dic.keys())
        #     if num[i] == item:
        #         dic[item] -= 1
        #         if dic[item] == 0:
        #             del dic[item]
        #         continue
        #     elif num[i] != item:
        #         idx = n - num[::-1].index(item) - 1 #这里别管是不是idx<i，因为dic证明了i后面总会出现
        #         num[i],num[idx] = num[idx],num[i]
        #         break
        # return int("".join(num))

        # mark
        # num = list(map(int, str(num)))
        # n = len(num)
        # mark = [None] * 10
        # for i in range(n):
        #     mark[num[i]] = i # 标记最后一次出现的位置
        # for k in range(n):
        #     for v in range(9, num[k], -1):
        #         if mark[v] is not None and mark[v] > k:
        #             num[mark[v]], num[k] = num[k], num[mark[v]]
        #             return int("".join(map(str,num)))
        # return int("".join(map(str,num)))

        # 单调栈
        st=[] #单调递增栈
        a=num
        ans=index=big=k=0
        old=[]  #save every bit
        while a:
            a,yu=divmod(a,10)
            old.append(yu)
            k-=1
            if yu>big:
                big,index=yu,k
            st.append((index,big))
        #从高位到低位扫描，能换就换，换一次，就不换了，加完
        w=-1
        while w>k:
            if old[w] < st[w][1]:
                #swap
                t=-st[w][0]-1
                old[w],old[t] = st[w][1],old[w]
                break
            w-=1
        c=1
        for i in old:
            ans += i*c
            c*=10
        return ans
