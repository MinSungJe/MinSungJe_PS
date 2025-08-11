TC = int(input())
for _ in range(TC):
    car = int(input())
    option = int(input())
    for _ in range(option):
        p, q = map(int, input().split())
        car += p * q
    print(car)