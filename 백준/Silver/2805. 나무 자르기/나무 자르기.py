N, M = map(int,input().split())
treelist = list(map(int,input().split()))

def find(start,end,target,treearray):
    mid = (start + end) // 2
    result = 0

    for i in range(len(treearray)):
        if treearray[i] - mid > 0:
            result += treearray[i] - mid
    
    if result == target or mid == start:
        return mid
    
    if result > target:
        return find(mid, end, target, treearray)
    
    if result < target:
        return find(start, mid, target, treearray)

print(find(0,max(treelist),M,treelist))