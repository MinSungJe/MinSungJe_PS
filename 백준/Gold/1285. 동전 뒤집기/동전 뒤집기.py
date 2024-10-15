# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
Map = [list(input()) for _ in range(N)]

# 전역변수 선언
INF = 401

# 열을 뒤집는 모든 경우 확인
result = INF
for filp in range(1<<N):
    value = 0
    for y in range(N):
        tail_value = 0
        for x in range(N):
            # 열이 뒤집혔는지 확인
            is_filp = filp & (1 << x)
            if is_filp:
                if Map[x][y] == 'H': tail_value += 1
            else:
                if Map[x][y] == 'T': tail_value += 1
        
        # T면이 과반수 이상이면, 뒤집어야 좋음(그리디)
        if tail_value > (N//2): value += (N-tail_value)
        else: value += tail_value
    
    # 최솟값 구하기
    result = min(result, value)

# 출력부
print(result)