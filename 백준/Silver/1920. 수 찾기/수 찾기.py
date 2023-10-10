def binary(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        
        # print(start, end, mid, target, array)

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1
        
    return None

N = int(input())
Ns = list(map(int,input().split()))

M = int(input())
Ms = list(map(int,input().split()))

Ns.sort()

for i in range(M):
    result = binary(Ns, Ms[i], 0, N-1)
    print('0' if result is None else '1')