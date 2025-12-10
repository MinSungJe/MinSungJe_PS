N = int(input())
numbers = list(map(int, input().split()))

seat = [False for _ in range(101)]
answer = 0
for number in numbers:
    if seat[number]: answer += 1
    seat[number] = True
    
print(answer)