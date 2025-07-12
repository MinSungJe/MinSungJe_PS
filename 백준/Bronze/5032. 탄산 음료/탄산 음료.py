# 입력부
e, f, c = map(int, input().split())

# 병 바꾸기
bottle = e+f
answer = 0
while bottle >= c:
    answer += bottle // c
    bottle = bottle // c + bottle % c

# 출력부
print(answer)