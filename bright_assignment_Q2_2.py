#bright_assignment_Q2_2.py

string = input("Enter a string = ")
freq = {}

for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

print("Character frequency dictionary:", freq)
