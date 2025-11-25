N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    you = A // B
    dad = A % B
    answer = f"You get {you} piece(s) and your dad gets {dad} piece(s)."
    print(answer)