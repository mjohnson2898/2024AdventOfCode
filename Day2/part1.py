safeReports = 0
file = open("Day2/input.txt", "r")
for line in file:
    line = line.strip().split(" ")
    safe = True
    i = 1
    increasing = True
    while i < len(line):
        a = int(line[i])
        b = int(line[i-1])
        curr = a-b
        if i == 1:
            increasing = True if curr > 0 else False
        else: 
            if curr > 0 and increasing == False:
                safe = False
                break
            if curr < 0 and increasing == True:
                safe = False
                break
        if a - b > 3 or a - b < -3 or a == b:
            safe = False
            break
        i += 1
    if safe:
        safeReports += 1

print(safeReports)