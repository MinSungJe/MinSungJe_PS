T = int(input())

for test_case in range(1,T+1):
    H, W, N = map(int,input().split())
    floor = 0
    room = 1
    for i in range(N):
        floor += 1
        if floor > H:
            room += 1
            floor = 1
    print(int(f"{floor:02d}{room:02d}"))
