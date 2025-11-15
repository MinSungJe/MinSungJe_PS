T = int(input())
for _ in range(T):
    N = int(input())
    people = list(int(input())-1 for _ in range(N))
    visited = [False for _ in range(N)]
    
    position = 0
    answer = 0
    while True:
        if position == N-1:
            break
        if visited[position]:
            answer = 0
            break

        visited[position] = True
        answer += 1
        position = people[position]

    print(answer)