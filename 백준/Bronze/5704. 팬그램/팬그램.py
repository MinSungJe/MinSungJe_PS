while True:
    sentence = input()
    if sentence == '*': break
    
    letters = set()
    for letter in sentence:
        if letter == ' ': continue
        letters.add(letter)
    
    print('Y' if len(letters) == 26 else 'N')