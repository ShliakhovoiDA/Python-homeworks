import json

with open("lesson_5_ex7.json", "w+", encoding="utf-8") as new_file_json:
    with open("lesson_5_ex7.txt", encoding="utf-8") as file:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in file}
        result = [profit, {"общая прибыль": round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                                  len([int(i) for i in profit.values() if int(i) > 0]))}]
    json.dump(result, new_file_json, ensure_ascii=False, indent=4)

# Списано, разобрано