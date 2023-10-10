def find(start, end, condition, arr):
    mid = (start + end) // 2
    result = 0

    for line in arr:
        result += (line // mid)
    

    # print(start, mid, end, condition, result)

    if result < condition:
        return find(start, mid, condition, arr)

    else:
        if start == mid:
            return mid
        else:
            return find(mid, end, condition, arr)



K,N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

print(find(1,max(lines)+1,N,lines))