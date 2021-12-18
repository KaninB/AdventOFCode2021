with open("02.txt") as f:
    lines = f.readlines()

pos = 0
aim = 0
depth = 0
for line in lines:
    comp = line.split(' ')
    action = comp[0]
    value = int(comp[1])
    if "up" == action:
        aim -= value
    elif "down" == action:
        aim += value
    else:
        depth += aim*value
        pos += value
total = pos*depth
print(total)