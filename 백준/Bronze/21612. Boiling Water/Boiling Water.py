N = int(input())
answer = 5 * N - 400
sea_level = 1 if answer < 100 else 0 if answer == 100 else -1
print(answer)
print(sea_level)