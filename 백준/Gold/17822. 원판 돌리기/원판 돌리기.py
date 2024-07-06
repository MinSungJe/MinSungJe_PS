# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M, T = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]


# 원판 적힌 수 합 구하는 함수
def sumMap(getMean=False):
    result = 0
    count = 0

    for i in range(N):
        for j in range(M):
            value = Map[i][j]
            if value == -1: continue # x는 건너뛰기
            result += value
            count += 1

    if getMean:
        if not count: return 0
        return result / count
    return result

# 원판 돌리는 함수
def rotate(x, d, k):
    # 원판 결정
    for num in range(x, N+1, x):
        idx = num-1
        
        temp = Map[idx][:]
        for i in range(M):
            pos = (i+k) % M
            if d == 0: Map[idx][pos] = temp[i]
            if d == 1: Map[idx][i] = temp[pos]

# 인접한 수 찾기
def find():
    change = [[False for _ in range(M)] for _ in range(N)]
    result = False

    for i in range(N):
        for j in range(M):
            if Map[i][j] == -1: continue # 이미 숫자가 지워진 경우
            
            # 같은 원반내에서 찾기
            j_ = (j+1) % M
            if Map[i][j] == Map[i][j_]: # 인접
                change[i][j], change[i][j_] = True, True

            # 다른 원반내에서 찾기
            if i == N-1: continue
            i_ = i+1
            if Map[i][j] == Map[i_][j]: # 인접
                change[i][j], change[i_][j] = True, True
    
    # 인접한 숫자가 있는 경우 전부 없애기(-1로 변경)
    for i in range(N):
        for j in range(M):
            if change[i][j]:
                Map[i][j] = -1
                result = True

    return result

# 원반의 평균값 구하고 숫자 조정하는 함수
def changeValue():
    mean = sumMap(getMean=True)

    for i in range(N):
        for j in range(M):
            value = Map[i][j]
            if value == -1: continue
            if value > mean: Map[i][j] -= 1
            if value < mean: Map[i][j] += 1

# 함수 호출
for _ in range(T):
    x, d, k = map(int, input().split())
    rotate(x, d, k) # 돌리기
    if not find(): # 인접한 수 찾기
        changeValue() # 인접한 숫자 없으면 값 바꾸기

# 출력부
print(sumMap())