T = int(input())
for _ in range(T):
    money = int(input())
    Q = money // 25
    D = (money % 25) // 10
    N = ((money % 25) % 10) // 5
    P = money % 5

    print(Q, D, N, P)