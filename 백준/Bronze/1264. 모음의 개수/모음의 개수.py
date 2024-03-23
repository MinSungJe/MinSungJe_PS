while 1:
    sentence = input()
    
    if sentence == '#': break
    result = 0
    for letter in sentence:
        if letter in ('a','e','i','o','u','A','E','I','O','U'): result += 1
    print(result)