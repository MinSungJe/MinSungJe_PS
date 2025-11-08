N = int(input())
for i in range(N):
    print(f"{' '*i}{'*'*(N-1-i)}*{'*'*(N-1-i)}")
for i in range(1, N):
    print(f"{' '*(N-1-i)}{'*'*(i)}*{'*'*(i)}")