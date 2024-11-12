def isPalin(letter):
    L = len(letter)
    result = True
    for i in range(L//2):
        if letter[i] != letter[L-1-i]: result = False
    
    return result

T = int(input())
for test_case in range(1, T+1):
    S = input()
    L = len(S)
    
    result = True
    for letter in (S, S[:L//2], S[(L//2)+1:]):
        if not isPalin(letter): result = False
    
    print(f"#{test_case} {'YES' if result else 'NO'}")