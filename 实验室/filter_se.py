import json

# single: not, X
# double: U, and

with open('D:\\study\\Master\\实验室\\se\\t0_0\\train.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
    formula = []
    formula_list = d['ltlftree']
    pre = formula_list
    while pre:
        print(pre[0])
        print(pre[1])
        pre = pre[1]

    # print(d['traces_pos'])
    print(len(d))
