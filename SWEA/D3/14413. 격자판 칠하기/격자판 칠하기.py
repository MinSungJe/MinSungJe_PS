T = int(input())

def getMap(X, Y, startMark, restMark):
    if (X+Y) % 2 == 0: return startMark
    else: return restMark

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    Map = [list(input()) for _ in range(N)]
    
    sharpStartResult = True
    dotStartResult = True
    
    for i in range(N):
        for j in range(M):
            if Map[i][j] == '?': continue
            if Map[i][j] != getMap(i, j, '#', '.'): sharpStartResult = False
            if Map[i][j] != getMap(i, j, '.', '#'): dotStartResult = False
    
    result = sharpStartResult or dotStartResult
    print(f"#{test_case} {'possible' if result else 'impossible'}")