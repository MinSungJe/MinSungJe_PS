brackets = ['(',')','[',']']
while 1:
    inputs = input()
    if inputs == '.':
        break
    bracket = []
    roundbrac = 0
    bigbrac = 0
    lastopend = ''
    balanced = False

    usedbracket = []

    for i in inputs:
        if i in brackets:
            bracket.append(i)

    for i in bracket:
        if i == '(':
            roundbrac += 1
            usedbracket.append(i)
        if i == ')':
            if usedbracket and usedbracket.pop() == '(':
                roundbrac -= 1
            else:
                roundbrac -= 1
                break
        if i == '[':
            usedbracket.append(i)
            bigbrac += 1
        if i == ']':
            if usedbracket and usedbracket.pop() == '[':
                bigbrac -= 1
            else:
                bigbrac -= 1
                break
        
        if roundbrac < 0 or bigbrac < 0:
            break

    if roundbrac == 0 and bigbrac == 0:
        balanced = True
    
    # print(bracket, usedbracket, roundbrac, bigbrac)
    print('yes' if balanced else 'no')