# 입력부
N = int(input())
# 숫자로 변환할 수 있으면 자료형을 변환하는 함수
def changeInt(data):
    if ord(data) >= 48 and ord(data) <= 57:
        return int(data)
    return str(data)
Map = [list(map(changeInt, input().split())) for _ in range(N)]

# 전역변수 선언
INF = 3126

# DFS
def DFS(X, Y, operator, value, isMax):
    # 탐색 종료
    if X == N-1 and Y == N-1: return calculator(Map[X][Y], operator, value)
    result = (-1*INF) if isMax else INF
    if X > N-1 or Y > N-1: return result
    
    # 다음 탐색
    if (X + Y) % 2 == 0:
        value_ = calculator(Map[X][Y], operator, value)
        for X_, Y_ in ((X+1, Y), (X, Y+1)):
            result = max(result, DFS(X_, Y_, operator, value_, isMax)) if isMax else min(result, DFS(X_, Y_, operator, value_, isMax))
        return result
    
    for X_, Y_ in ((X+1, Y), (X, Y+1)):
        operator_ = Map[X][Y]
        result = max(result, DFS(X_, Y_, operator_, value, isMax)) if isMax else min(result, DFS(X_, Y_, operator_, value, isMax))
    return result

# 계산하는 함수
def calculator(value, operator, result):
    if operator == '+': return result + value
    if operator == '-': return result - value
    if operator == '*': return result * value

# 함수 호출 및 출력부
max_result = DFS(0, 0, '+', 0, True)
min_result = DFS(0, 0, '+', 0, False)
print(max_result, min_result)