nums = [0] * 9
for i in range(9):
    num = int(input())
    nums[i] = num

max = 0
idx = 0
for i in range(9):
    if max < nums[i]:
        max = nums[i]
        idx = i+1

print(max)
print(idx)