T = int(input())
for _ in range(T):
    A, B = map(list, input().split())
    
    answer = 'Possible'
    if len(A) != len(B): answer = 'Impossible'
    else:
        A.sort()
        B.sort()
        for i in range(len(A)):
            if A[i] != B[i]: answer = 'Impossible'
    
    print(answer)