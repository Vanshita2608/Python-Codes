#bright_assignment_Q2_1.py

n = int(input("Enter the number of students: "))
marks = []
for i in range(n):
    m = int(input("Enter marks out of 100 for student {}: ".format(i+1)))
    marks.append(m)

freq_dict = {"0-39": 0,"40-60": 0,"61-80": 0,"81-100": 0}

for m in marks:
    if m >= 0 and m <= 39:
        freq_dict["0-39"] += 1
    elif m >= 40 and m <= 60:
        freq_dict["40-60"] += 1
    elif m >= 61 and m <= 80:
        freq_dict["61-80"] += 1
    elif m >= 81 and m <= 100:
        freq_dict["81-100"] += 1

print("Frequency count of marks range:")
for key, value in freq_dict.items():
    print("{}: {}".format(key, value))
