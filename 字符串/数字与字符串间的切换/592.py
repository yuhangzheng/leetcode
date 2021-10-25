class Solution:
    def fractionAddition(self, expression: str) -> str:
        res = str()  # 用于存储每个数据
        zi, mu = list(), list()  # 存储分子/分母
        res = expression.replace('-', '+-').split('+')
        n, sum_zi = len(res), 0

        # 分子、分母存在两个list中
        for num in res:
            if num != '':
                zi_num, mu_num = num.split('/')
                zi.append(zi_num)
                mu.append(mu_num)

        # 求分母的最小公倍数
        a = int(mu[0])
        for i in range(1, len(mu)):
            b = int(mu[i])
            pro = a * b
            while (b > 0):
                a, b = b, a % b
            a = pro / a

        # 通分加减
        for i in range(len(zi)):
            sum_zi += int(zi[i]) * a / int(mu[i])

        # 化简，求分子分母最大公约数
        sim_zi = abs(int(sum_zi))
        sim_mu = a
        while (sim_mu > 0):
            sim_zi, sim_mu = sim_mu, sim_zi % sim_mu

        sum_zi = int(sum_zi) / sim_zi
        a = a / sim_zi
        return (str(int(sum_zi)) + '/' + str(int(a)))