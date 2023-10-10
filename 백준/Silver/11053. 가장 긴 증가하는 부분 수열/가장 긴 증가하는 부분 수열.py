def BS(num):
    l = 0
    r = len(K)-1
    answer = len(K)
    
    while l <= r:
        m = (l+r) // 2
        #print(K,l,r)
        
        if K[m] < num:
            l = m+1
        else:
            answer = m
            r = m-1
    return answer


# O(NlogN) 풀이
N = int(input())
numlist = list(map(int,input().split()))
numlist = [0] + numlist
LIS = [0 for _ in range(N+1)]
K = [0]

for i in range(1,N+1):
    # O(logN) 부분 : 이분탐색 이용
    LIS[i] = BS(numlist[i])
    if BS(numlist[i]) + 1 > len(K):
        K.append(numlist[i])
    else:
        K[BS(numlist[i])] = numlist[i]
    
print(max(LIS))