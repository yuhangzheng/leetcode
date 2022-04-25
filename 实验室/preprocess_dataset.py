
dict = {
        " zero ": " 0 ", " one ": " 1 ", " two ": " 2 ", " three ": " 3 ", " four ": " 4 ", " five ": " 5 ",
        " six ": " 6 ", " seven ": " 7 ", " eight ": " 8 ", " nine ": " 9 ", " ten ": " 10 ", " eleven ": " 11 ",
        " twelve ": " 12 ", " thirteen ": " 13 ", " fourteen ": " 14 ", " fifteen ": " 15 ", " sixteen ": " 16 ",
        " seventeen ": " 17 ", " eighteen ": " 18 ", " nineteen ": " 19 ", " twenty ": " 20 ",
        " twice ": " 2 ", " half ": " 0.5 ", " third ": " 3 ",
        }

with open('D:/study/Master/实验室/QA/grade-school-math-master/grade-school-math-master/grade_school_math/data/train.jsonl', 'r') as f:
    tmp = []
    for line in f:
        tmp.append(eval(line))

with open("D:/study/Master/实验室/QA/grade-school-math-master/grade-school-math-master/dataset/train.jsonl", 'w+', encoding='utf-8') as w:
    for i in range(len(tmp)):
        for key in dict.keys():
            if key in tmp[i].get("question"):
                tmp[i]["question"] = tmp[i].get("question").replace(key, dict[key])
        w.write(str(tmp[i]))
        w.write('\n')



