new_dict = {}
with open("lesson_5_ex6.txt", "r", encoding="utf-8") as file:
    for line in file:
        subject, time = line.split(':')
        sum_for_subject: int = sum(map(int, "".join([i for i in time if i == ' ' or '9' >= i >= '0']).split()))
        new_dict[subject] = sum_for_subject
print(f"{new_dict}")