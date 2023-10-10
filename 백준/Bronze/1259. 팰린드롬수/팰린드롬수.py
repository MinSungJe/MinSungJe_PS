num = input()
while int(num):
    print('yes' if num == num[::-1] else 'no')
    num = input()