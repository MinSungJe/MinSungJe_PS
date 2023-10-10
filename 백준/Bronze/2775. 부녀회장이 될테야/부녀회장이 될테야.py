apartment = [[0]*15 for _ in range(15)]
def room(k,n):
    if k == 0:
        apartment[k][n] = n+1
        return apartment[k][n]
    
    if apartment[k][n] != 0:
        return apartment[k][n]
    
    for i in range(n+1):
        apartment[k][n] += room(k-1,i)
    return apartment[k][n]

T = int(input())

for test_case in range(1,T+1):
    floor = int(input())
    roomnum = int(input())

    print(room(floor,roomnum-1))