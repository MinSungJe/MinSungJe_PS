# TC
T = int(input())
for _ in range(T):
    # 입력부
    s, p = input().split()

    # 결과값 구하기
    answer = 0
    split = s.split(p)
    answer += len(split) - 1
    for partition in split: answer += len(partition)
    
    # 출력부
    print(answer)