price = int(input())
N = int(input())
sum = 0
for stuff_num in range(N):
    name,stuffPrice = map(int, input().split())
    sum += name * stuffPrice
print("Yes" if sum == price else "No")