N = list(map(int, input().split()))

answer = N == sorted(N)
print('Good' if answer else 'Bad')