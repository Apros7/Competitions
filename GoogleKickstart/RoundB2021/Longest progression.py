t = int(input())
for case in range(1, t+1):
    N = int(input())
    numbers = "".join(input().split(" "))
    previous_diff = int(numbers[1])-int(numbers[0])
    max_count = 0
    current_count = 1
    for i in range(1, N-1):
        diff = int(numbers[i+1])-int(numbers[i])
        if (previous_diff != diff):
            new_first_value = int(numbers[i+1]) - previous_diff
            x = i
            new_list = numbers[i] + str(new_first_value) + numbers[i+2:]
            print(new_list)
            while (int(new_list[x+1])-int(new_list[x])) == previous_diff:
                x += 1
                current_count += 1
            max_count = max(current_count, max_count)
            current_count = 1
        else:
            current_count += 1
            max_count = max(current_count, max_count)

        previous_diff = diff



    print(f"Case #{case}: {max_count}")