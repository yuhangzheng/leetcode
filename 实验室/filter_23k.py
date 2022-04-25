import json
import re

# ape210k.json   CM17k.json   Math_23K.json   MAWPS.json

with open('D:/study/Master/实验室/QA/dataset/train_23k.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
    not_match = []

    # Math_23K
    for i in range(len(d)):
        question = d[i].get("original_text")
        numbers = re.findall(r"[0-9.]+", d[i].get("equation"))
        for number in numbers:
            if number not in question:
                print(question)
                print(number)
                print(d[i].get("equation"))
                not_match.append(i)
    print(len(set(not_match)))
    print(len(d))
