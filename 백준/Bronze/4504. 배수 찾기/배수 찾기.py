n = int(input())
while True:
    number = int(input())
    if not number: break
    print(f'{number} is NOT a multiple of {n}.' if number % n else f'{number} is a multiple of {n}.')