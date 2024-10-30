# 모듈 불러오기
import sys

# 입력부
N = int(input())

# 가우스 합 구하기
original_sum = N * (N-1) // 2

# 한 숫자씩 입력받아 합 계산
changed_sum = 0
while True:
    letter = sys.stdin.read(1)
    if letter == '': break

    number = ''
    while letter != ' ' and letter != '':
        number += letter
        letter = sys.stdin.read(1)
    
    changed_sum += int(number)

# 출력부
result = changed_sum - original_sum
print(result)