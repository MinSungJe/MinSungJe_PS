# TC
T = int(input())
for test_case in range(T):
    # 입력부
    J, N = map(int, input().split())

    # 박스에 담을 수 있는 사탕개수 계산
    box = list()
    for _ in range(N):
        R, C = map(int, input().split())
        box.append(R*C)
    
    # 박스 정렬
    box.sort(key=lambda x:-x)

    # 모든 사탕을 담을 때까지 상자 사용해보기
    result = 0
    for i in range(N):
        J -= box[i]
        result += 1
        if J <= 0: break
    
    # 출력부
    print(result)