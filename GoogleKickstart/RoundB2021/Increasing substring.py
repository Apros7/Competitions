t = int(input())
dict = {"begin": -1, "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6,
"h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o":14, 
"p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, 
"w": 22, "x": 23, "y": 24, "z": 25}
for case in range(1, t+1):
    length = input()
    string = input().lower()
    pointer = 0
    last_letter = "begin"
    listOfPointers = []
    for letter in string:
        if dict[last_letter] < dict[letter]:
            pointer += 1
            listOfPointers.append(pointer)
        else:
            pointer = 1
            listOfPointers.append(pointer)
        last_letter = letter
    print(f"Case #{case}: ", end="")
    print(*listOfPointers)
