# 입력부
N = int(input())

# 초기값 선언
mooLength = []
length = 3
idx = 0

# 길이 배열 채우기
while length < N:
    mooLength.append(length)
    idx += 1
    length = (2 * length) + (idx + 3)

# moo 구성 -> mooLength(마지막 - 1) + (마지막인덱스번호 + 3) + mooLength(마지막 - 1)
# 분할정복
def MOO(num):
    global idx

    # 분할 완료
    if num == 1: return 'm'
    if num == 2: return 'o'
    if num == 3: return 'o'

    rindex = mooLength[idx-1] + (idx + 3)

    if num <= mooLength[idx-1]:
        idx -= 1
        return MOO(num)
    elif num <= rindex:
        if num == mooLength[idx-1] + 1: return 'm'
        else: return 'o'
    elif num > rindex:
        idx -= 1
        return MOO(num - rindex)

# 출력부
print(MOO(N))