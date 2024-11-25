# 입력부
A = int(input())
B = int(input())

# 초기값 선언
notSosu = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
DP = [[[-1 for _ in range(18)] for _ in range(18)] for _ in range(18)]

# 둘다 합성수로 득점한 경우 곱하기
def DFS(idx, Acount, Bcount):
    global A, B

    # 탐색 종료
    if idx >= 18:
        result = 1
        if Acount in notSosu and Bcount in notSosu:
            result *= (A/100) ** Acount
            result *= ((100-A)/100) ** (18-Acount)
            result *= (B/100) ** Bcount
            result *= ((100-B)/100) ** (18-Bcount)
            return result
        else: return 0
    
    # 메모이제이션 확인
    if DP[idx][Acount][Bcount] != -1: return DP[idx][Acount][Bcount]
    
    # 다음 탐색
    result = 0

    # 모든 득점 경우에 대해 확인
    for A_, B_ in ((Acount, Bcount), (Acount+1, Bcount), (Acount, Bcount+1), (Acount+1, Bcount+1)):
        result += DFS(idx+1, A_, B_)
    
    # 메모이제이션
    DP[idx][Acount][Bcount] = result
    return result

# 함수 호출 및 출력부
result = DFS(0, 0, 0)
print(1-result)