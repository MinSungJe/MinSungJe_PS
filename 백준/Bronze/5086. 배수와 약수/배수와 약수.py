while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0: break
    
    answer = "neither"
    for a_ in range(a, b+1, a):
        if a_ == b: answer = "factor"
    for b_ in range(b, a+1, b):
        if b_ == a: answer = "multiple"

    print(answer)