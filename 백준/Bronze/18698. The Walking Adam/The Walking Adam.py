N = int(input())
for _ in range(N):
    adam = input()
    answer = 0
    for step in adam:
        if step != 'U': break
        answer += 1
    print(answer)