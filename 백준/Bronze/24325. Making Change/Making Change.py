# 잔돈 받는 함수
def getChange(change):
    change = int(change)
    v = change // 50
    change %= 50

    w = change // 20
    change %= 20

    x = change // 10
    change %= 10

    y = change // 5
    change %= 5

    z = change

    return v, w, x, y, z

# 입력부
n = int(input())
for _ in range(n):
    cost, payment = map(float, input().split())

    # 거스름돈 단위 구하기
    v, w, x, y, z = getChange(payment - cost)
    
    # 출력부
    print(f"{v}-$50, {w}-$20, {x}-$10, {y}-$5, {z}-$1")