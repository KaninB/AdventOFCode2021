with open("02.txt") as f:
    lines = f.readlines()

pos = 0
depth = 0
for line in lines:
    comp = line.split(' ')
    if "up" == comp[0]:
        depth -= int(comp[1])
    elif "down" == comp[0]:
        depth += int(comp[1])
    else:
        pos += int(comp[1])
total = pos*depth