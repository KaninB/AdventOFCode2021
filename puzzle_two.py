cnt = -1 #Initialize counting variable
nums = [] #Using a list due to task specification

with open("01.txt") as f:
    lines = f.readlines()
    for line in lines:
        nums += [int(line)]

prev = -1
for i in range(len(nums)-2):
    curr = nums[i] + nums[i+1] + nums[i+2]
    if curr > prev:
        cnt += 1
    prev = curr

print(cnt)