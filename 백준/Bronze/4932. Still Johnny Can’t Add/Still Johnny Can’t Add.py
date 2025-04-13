# TC
T = int(input())
for test_case in range(1, T+1):
    # 입력부
    N = int(input())
    Map = [list(map(int, input().split())) for _ in range(N)]

    # 처음 줄 간격 기록
    gap = list()
    for i in range(N-1):
        value = Map[0][i+1] - Map[0][i]
        gap.append(value)

    # 덧셈표 가능 여부 확인
    result = 'YES'
    for row in range(1, N):
        for i in range(N-1):
            if Map[row][i] + gap[i] != Map[row][i+1]: result = 'NO'

    # 출력부
    print(f"{test_case}. {result}")