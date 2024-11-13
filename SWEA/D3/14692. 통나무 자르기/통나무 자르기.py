TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    print(f"#{test_case} {'Alice' if N % 2 == 0 else 'Bob'}")