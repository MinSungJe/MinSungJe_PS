N = int(input())
for i in range(1, N+1):
    print(f"{' ' * (N-i)}{'*' * (2*i-1)}")