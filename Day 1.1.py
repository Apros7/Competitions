with open("Day 1.1.input", "r", newline="") as file:
    max_calorie = 0
    temp_value = 0
    lines = file.readlines()
    for line in lines:
        line = line.strip("\n")
        print(line)
        print(temp_value)
        if line == "":
            max_calorie = max(max_calorie, temp_value)
            temp_value = 0
        else:
            temp_value += int(line)
    print(max_calorie)
