import json
import re

# ape210k.json   CM17k.json   Math_23K.json   MAWPS.json

with open('D:/study/Master/实验室/QA/dataset/origin/CM17k.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
    not_match = []

    # MAWPS
    for i in range(len(d)):
        question = d[i].get("original_text")
        numbers = re.findall(r"[0-9.]+", d[i].get("equation"))
        for number in numbers:
            if ".0" in number:
                number = number[:-2]
            if number not in question:
                if number == "1" or number == "3.14":
                    pass
                else:
                    print(question)
                    print(d[i].get("equation"))
                    print(number)
                    not_match.append(i)
    print(len(set(not_match)))
    print(len(d))
