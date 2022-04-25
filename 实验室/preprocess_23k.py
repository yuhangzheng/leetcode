import json
import re

dict = {
        "零": "0", "一": "1", "二": "2", "三": "3", "四": "4", "五": "5",
        "六": "6", "七": "7", "八": "8", "九": "9", "十": "10", "两": "2",
        }

with open('D:/study/Master/实验室/QA/dataset/origin/Math_23K.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

with open("D:/study/Master/实验室/QA/dataset/train_23k.json", 'w+', encoding='utf-8') as w:
    for i in range(len(d)):
        numbers = re.findall(r"[0-9.]+", d[i].get("equation"))
        if "3.14" in numbers:
            if "3.14" not in d[i].get("original_text"):
                d[i]["original_text"] = "(圆周率取3.14)" + d[i].get("original_text")
                d[i]["segmented_text"] = "(圆周率 取 3.14)" + d[i].get("segmented_text")

        for key in dict.keys():
            if key in d[i].get("original_text"):
                d[i]["original_text"] = d[i].get("original_text").replace(key, dict[key])
                d[i]["segmented_text"] = d[i].get("segmented_text").replace(key, dict[key])

    d = json.dumps(d, ensure_ascii=False)
    w.write(d)
