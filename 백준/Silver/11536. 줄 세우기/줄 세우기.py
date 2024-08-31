# 입력부
N = int(input())
names = [input() for _ in range(N)]

# 오름차순 정리
increase_names = names[:]
increase_names.sort()

# 내림차순 정리
decrease_names = names[:]
decrease_names.sort(reverse=True)

# 확인
result = 'NEITHER'
increased = True
decreased = True
for i in range(N):
    if increase_names[i] != names[i]: increased = False
    if decrease_names[i] != names[i]: decreased = False
if increased: result = 'INCREASING'
if decreased: result = 'DECREASING'

# 출력부
print(result)