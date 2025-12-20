# TC
C = int(input())
for test_case in range(1, C+1):
    # 입력부
    [N, *scores] = list(map(int, input().split()))
    
    # 평균 구하기
    average = sum(scores) / N

    # 평균보다 높은 인원 구하기
    good_student_count = 0
    for score in scores:
        if score > average: good_student_count += 1
    
    # 비율 계산 및 출력부
    ratio = good_student_count / N
    answer = f"{ratio * 100:.3f}%"
    print(answer)