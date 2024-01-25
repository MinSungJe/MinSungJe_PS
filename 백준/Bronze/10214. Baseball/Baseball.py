T = int(input())
for test_case in range(1, T+1):
    team1 = 0
    team2 = 0
    for _ in range(9):
        A, B = map(int, input().split())
        team1 += A
        team2 += B
    if team1 > team2: print("Yonsei")
    elif team1 < team2: print("Korea")
    else: print("Draw")