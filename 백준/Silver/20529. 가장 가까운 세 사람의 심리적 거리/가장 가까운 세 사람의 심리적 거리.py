T = int(input())
for test_case in range(1,T+1):
    # 초기값 선언
    MBTI = {}
    count = []
    result = 13

    # 입력부
    N = int(input())
    MBTI = list(input().split())

    # 비둘기집
    if N > 32:
        print(0)
        continue

    # 계산
    for i in range(len(MBTI)):
        for j in range(i+1, len(MBTI)):
            for k in range(j+1, len(MBTI)):
                temp = 0
                for idx in range(4):
                    if MBTI[i][idx] != MBTI[j][idx]: temp += 1
                    if MBTI[j][idx] != MBTI[k][idx]: temp += 1
                    if MBTI[i][idx] != MBTI[k][idx]: temp += 1
                if temp < result: result = temp
    
    # 출력부
    print(result)