# 입력부
N = int(input())
test = input()

# 초기값 선언
one, two, three = 0, 0, 0
one_answer = ['A', 'B', 'C']
two_answer = ['B', 'A', 'B', 'C']
three_answer = ['C', 'C', 'A', 'A', 'B', 'B']

# 답안지 확인
for i in range(N):
    if test[i] == one_answer[i%3]: one += 1
    if test[i] == two_answer[i%4]: two += 1
    if test[i] == three_answer[i%6]: three += 1

# 높은 사람 확인
max_value = max(one, two, three)

# 출력부
print(max_value)
if max_value == one: print('Adrian')
if max_value == two: print('Bruno')
if max_value == three: print('Goran')