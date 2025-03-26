# 입력부
N = int(input())
for _ in range(N):
    problem = input()
    if problem == 'P=NP':
        print('skipped')
        continue

    a, b = map(int, problem.split('+'))
    print(a+b)