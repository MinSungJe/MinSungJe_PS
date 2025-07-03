# 입력부
a, b = map(int, input().split())
start_position = input()

# 위치 변환 함수
def get_number_position(position):
    x = ord(position[0])-96
    y = int(position[1])

    return (x, y)

def get_string_position(X, Y):
    x = chr(X+96)
    y = str(Y)
    return x+y

def check_is_enable(X, Y): return 1 <= X <= 8 and 1 <= Y <= 8

# 나이트 이동 확인
answer_set = set()
X, Y = get_number_position(start_position)
if check_is_enable(X+a, Y+b): answer_set.add(get_string_position(X+a, Y+b))
if check_is_enable(X+a, Y-b): answer_set.add(get_string_position(X+a, Y-b))
if check_is_enable(X-a, Y+b): answer_set.add(get_string_position(X-a, Y+b))
if check_is_enable(X-a, Y-b): answer_set.add(get_string_position(X-a, Y-b))
if check_is_enable(X+b, Y+a): answer_set.add(get_string_position(X+b, Y+a))
if check_is_enable(X+b, Y-a): answer_set.add(get_string_position(X+b, Y-a))
if check_is_enable(X-b, Y+a): answer_set.add(get_string_position(X-b, Y+a))
if check_is_enable(X-b, Y-a): answer_set.add(get_string_position(X-b, Y-a))
answer = list(answer_set)
answer.sort()

# 출력부
print(len(answer))
print(*answer)