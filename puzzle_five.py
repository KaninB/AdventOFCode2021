with open("03.txt") as f:
    lines = f.readlines()

majority = len(lines)/2
digits = len(lines[0]) #all lines appear to be the same size

#Populate Dictionary
ones_count_dict = {}
for i in range(digits-1):
    ones_count_dict[str(i)] = 0

#Determine Frequencies
for line in lines:
    line = line.strip() #Need to remove new line characters
    for i in range(len(line)):
        if int(line[i]) == 1:
            ones_count_dict[str(i)] += 1
print(ones_count_dict)
#Convert to String
gamma = ""
epsilon = ""
for key in ones_count_dict:
    outcome = 0
    if ones_count_dict[key] > 1000-ones_count_dict[key]:
        outcome = 1
    gamma += str(outcome)
    epsilon += str(abs(outcome-1))  

#Convert to Binary and then Integer
gamma = int(gamma,2)
epsilon = int(epsilon,2)
print(gamma*epsilon)