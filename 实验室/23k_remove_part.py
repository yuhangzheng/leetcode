import json
import re

with open('D:/study/Master/实验室/QA/dataset/train_23k.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
    for i in range(len(d)):
        if '/' in d[i]['ans']:
            a = d[i]['ans']
            j = 0
            num1 = ''
            while a[j] != '(':
                num1 += a[j]
                j += 1
            num2 = eval(a[j:])
            if num1 != '':
                num1 = eval(num1)
                d[i]['ans'] = str(num1+num2)
            else:
                d[i]['ans'] = str(num2)


with open("D:/study/Master/实验室/QA/dataset/train_23k.json", 'w+', encoding='utf-8') as w:
    d = json.dumps(d, ensure_ascii=False)
    w.write(d)
