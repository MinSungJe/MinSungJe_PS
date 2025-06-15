def factorial(number):
    if number == 0: return 1
    return number * factorial(number-1)

def get_e(number):
    answer = 0
    
    for i in range(number+1):
        answer += 1 / factorial(i)
    
    return answer

print('n e')
print('- -----------')
for i in range(10):
    e_value = get_e(i)
    if i == 0 or i == 1:
        print(f'{i} {int(e_value)}')
    elif i == 2:
        print(f'{i} {e_value:.1f}')
    else:
        print(f'{i} {e_value:.9f}')