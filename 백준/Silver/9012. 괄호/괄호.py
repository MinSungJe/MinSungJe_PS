T = int(input())
for test_case in range(1,T+1):
    letter = input()
    count = 0
    VPS = True
    for i in letter:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        
        if count < 0:
            VPS = False
            break
    
    if count != 0:
        VPS = False
    
    print('YES' if VPS else 'NO')