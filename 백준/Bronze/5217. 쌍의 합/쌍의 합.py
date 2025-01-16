# 입력부
T = int(input())
for _ in range(T):
    n = int(input())
    
    # 쌍 구하기
    result = list()
    for i in range(1, n//2+1):
        rest = n-i
        if i == rest: continue
        result.append(f"{i} {rest}")
    
    # 출력부
    print(f"Pairs for {n}: {', '.join(result)}")