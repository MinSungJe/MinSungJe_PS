# 저장배열 선언
result = [0 for _ in range(101)]

# 초기값 채우기
result[1] = 1
result[2] = 1
result[3] = 1
result[4] = 2
result[5] = 2

# 나머지 값 채우기
for i in range(6,101):
    result[i] = result[i-5] + result[i-1]

# test_case 구현
T = int(input())
for test_case in range(1,T+1):
    # 출력부
    print(result[int(input())])