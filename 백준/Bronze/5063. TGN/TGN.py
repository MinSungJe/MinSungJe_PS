T = int(input())
for _ in range(T):
    r, e, c = map(int, input().split())
    answer = "does not matter"
    if r > (e-c): answer = "do not advertise"
    if r < (e-c): answer = "advertise"
    print(answer)