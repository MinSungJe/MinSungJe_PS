T = int(input())
for _ in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(sum(numbers))