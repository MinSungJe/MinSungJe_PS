# 입력부
letter = list(input())

# 초기값 선언
cow = {
    65: [],
    66: [],
    67: [],
    68: [],
    69: [],
    70: [],
    71: [],
    72: [],
    73: [],
    74: [],
    75: [],
    76: [],
    77: [],
    78: [],
    79: [],
    80: [],
    81: [],
    82: [],
    83: [],
    84: [],
    85: [],
    86: [],
    87: [],
    88: [],
    89: [],
    90: [],
}
for i in range(52): cow[ord(letter[i])].append(i+1)

# 두 경로가 만나는 경로인지 확인하는 함수
def checkIsMeet(a1, a2, b1, b2):
    if a1 < b1 < a2:
        if b2 < a1 or b2 > a2: return True
    if a1 < b2 < a2:
        if b1 < a1 or b1 > a2: return True
    return False

# 모든 소의 경우 체크
result = 0
for cow1 in range(65, 91):
    for cow2 in range(cow1+1, 91):
        if checkIsMeet(cow[cow1][0], cow[cow1][1], cow[cow2][0], cow[cow2][1]): result += 1

# 출력부
print(result)