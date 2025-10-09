letter = input()

answers = {
    '(1)': 0,
    '()1': 1,
    '1()': 1,
    '1)(': 1,
    ')1(': 2,
    ')(1': 1
}

answer = answers[letter]
print(answer)