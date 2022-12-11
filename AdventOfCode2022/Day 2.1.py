dict = {"X": 1, "Y": 2, "Z": 3}
dict2 = {"A": "X", "B": "Y", "C": "Z"}
with open("Day 2.1.input", "r") as file:
    score = 0
    for line in file:
        line = line.strip("\n")
        one, two = line.split()
        print(one, two)
        if two == "Y":
            score += 3 + dict[dict2[one]]
        elif two == "Z":
            score += 6
            if one == "A":
                score += 2
            elif one == "B":
                score += 3
            else:
                score += 1
        else:
            if one == "A":
                score += 3
            elif one == "B":
                score += 1
            else:
                score += 2
        

    print(score)

        
