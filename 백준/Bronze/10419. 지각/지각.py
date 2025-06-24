T = int(input())
for _ in range(T):
    d = int(input())
    for time in range(10000):
        if d < time*time + time: break
    print(time-1)