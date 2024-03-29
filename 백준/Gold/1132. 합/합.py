# 입력부
N = int(input())
words = [list(input()) for _ in range(N)]

# 문자를 숫자로 바꿔주는 함수
def changeLetter(letter):
    if letter == 'A': return 0
    if letter == 'B': return 1
    if letter == 'C': return 2
    if letter == 'D': return 3
    if letter == 'E': return 4
    if letter == 'F': return 5
    if letter == 'G': return 6
    if letter == 'H': return 7
    if letter == 'I': return 8
    if letter == 'J': return 9

# 초기값 선언
value = [[0, True] for _ in range(10)]

# value 배열 채우기
for word in words:
    m = 1
    value[changeLetter(word[0])][1] = False # 첫 번째 글자 표시
    for i in range(len(word)-1, -1, -1):
        value[changeLetter(word[i])][0] += m
        m *= 10

# value 배열 정렬
value.sort(reverse=True)

# 0 할당하기
if not value[9][1]: # 현재는 0이 될 수 없음
    for i in range(8, -1, -1): # 0이 될 수 있는 가장 가까운 값 찾기
        if value[i][1]: # 값을 찾으면 맨 뒤로 보냄
            temp = value[i][:]
            del value[i]
            value.append(temp)
            break

# 결과값 도출 및 출력부
result = 0
for i in range(10):
    result += value[i][0] * (9-i)
print(result)