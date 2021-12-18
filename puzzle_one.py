cnt = -1 #Count of deeper measurements with offset
prev = -1 #start current value at NaN to replace
with open("01.txt") as f:
    nums = f.readlines()
    print(len(nums))
    for line in nums:
        curr = int(line)
        if curr > prev:
            cnt += 1
        prev = curr

print(cnt)