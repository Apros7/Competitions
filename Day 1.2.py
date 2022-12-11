with open("Day 1.1.input", "r", newline="") as file:
    max_calorie = []
    temp_value = 0
    lines = file.readlines()
    for line in lines:
        line = line.strip("\n")
        if line == "":
            max_calorie.append(temp_value)
            temp_value = 0
        else:
            temp_value += int(line)
    print(sorted(max_calorie)[-3:])
    print(sum(sorted(max_calorie)[-3:]))

