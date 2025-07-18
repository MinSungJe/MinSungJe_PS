n, T = map(int, input().split())
times = list(map(int, input().split()))
answer = 0
value = 0
for i in range(n):
    value += times[i]
    if value > T: break
    answer += 1

print(answer)