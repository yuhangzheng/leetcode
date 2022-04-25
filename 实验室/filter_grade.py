import json
import re

with open('D:/study/Master/实验室/QA/grade-school-math-master/grade-school-math-master/dataset/train.jsonl', 'r', encoding='utf-8') as f:
    tmp = []
    not_match = []
    for line in f:
        tmp.append(eval(line))

    for i in range(len(tmp)):
            question = tmp[i].get("question")
            equations = re.findall(r"<<[0-9.+\-*/=()]+>>", tmp[i].get("answer"))
            final = tmp[i].get("answer").split(" ")[-1]

            for j, equation in enumerate(equations):
                numbers = re.findall(r"[0-9.]+", equation)
                for number in numbers[:-1]:
                    if number not in question:
                        rem = equations[0:j]
                        other_num = []
                        for other_equa in rem:
                            other_num += re.findall(r"[0-9.]+", other_equa)
                        if number not in other_num and number != final:
                            # print(equation)
                            # print(str(i) + " : " + "que: " + question + " equ: " + str(equations) + " final: " + final + " missing numbers:" + number)
                            not_match.append(i)
                            break
    print(len(set(not_match)))
    print(len(tmp))
