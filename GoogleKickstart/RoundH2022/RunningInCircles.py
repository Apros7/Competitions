N = int(input())
for case in range(1, N+1):
    trackLen, runningTimes = [int(x) for x in input().split()]
    laps, current_distance, current_direction = 0, 0, "C"
    for sprint in range(runningTimes):
        inp = input().split()
        distance, direction = int(inp[0]), str(inp[1])

        if direction == current_direction:
            current_distance += distance
        else:
            current_distance -= distance

        if current_distance <= trackLen:
            current_direction = direction
            current_distance = abs(current_distance)

        while current_distance >= trackLen:
            current_distance -= trackLen
            laps += 1
        
    print(f"Case #{case}: {laps}")