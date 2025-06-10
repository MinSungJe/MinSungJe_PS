# 입력부
n, k = map(int, input().split())

# 초기값 선언
answer = []

# DFS
def DFS(prev):
    value = sum(prev)
    # 탐색 종료
    if value > n: return
    if value == n:
        answer.append(prev)
        return
    
    # 다음 탐색
    for plus in (1,2,3):
        DFS(prev+[plus])

# 함수 호출 및 출력부
DFS([])
if len(answer) < k: print(-1)
else: print('+'.join(list(map(str, answer[k-1]))))