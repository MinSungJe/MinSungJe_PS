# 입력부
expression = input()

# 초기값 선언
operator = ['+', '-', '*', '/', '(', ')']
stack = []

# 스택이용 후위표기법 출력
for letter in expression:
    if letter not in operator: print(letter, end='')
    else:
        if letter == '(':
            stack.append(letter)
        if letter == ')':
            while True:
                if stack[-1] == '(':
                    stack.pop()
                    break
                else:
                    print(stack.pop(), end='')
        if letter == '*' or letter == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                print(stack.pop(), end='')
            stack.append(letter)
        if letter == '+' or letter == '-':
            while stack and stack[-1] != '(':
                print(stack.pop(), end='')
            stack.append(letter)
while stack: print(stack.pop(), end='')