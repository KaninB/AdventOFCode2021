"""Example for one number needed, script is modified when needed"""

with open("03.txt") as f:
    lines = f.readlines()

#Populate Dictionary
ones_count = 0
i = 0
entries = len(lines)
while entries > 1:
    #Determine Frequencies
    for line in lines:
        line = line.strip() #Need to remove new line characters
        if int(line[i]) == 1:
            ones_count += 1

    #Determine Case
    print(ones_count, entries-ones_count)
    if ones_count < entries-ones_count: #Switch to >= for other metric
        case = "1"
    else:
        case = "0"

    #Remove Bad Entries
    line_idx = 0
    while line_idx < len(lines):
        entries = len(lines)
        curr = lines[line_idx]
        if curr[i] != case and entries > 1:
            lines.remove(curr)
            line_idx -= 1
        line_idx += 1
    i += 1
    ones_count = 0
    entries = len(lines)

print(lines)
o2 = "101010101111"
co2 = "010111011101"
o2 = int(o2,2)
co2 = int(co2,2)
print(o2*co2)
