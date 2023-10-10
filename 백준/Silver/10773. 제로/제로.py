from collections import deque
nums = deque()

T = int(input())
for test_case in range(1,T+1):
    num = int(input())
    if num != 0:
        nums.append(num)
    else:
        nums.pop()

print(sum(nums))