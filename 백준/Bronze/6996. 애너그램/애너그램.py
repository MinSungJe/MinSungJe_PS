T = int(input())
for _ in range(T):
    A, B = input().split()

    A_list = [0 for _ in range(26)]
    B_list = [0 for _ in range(26)]
    for a in A: A_list[ord(a)-97] += 1
    for b in B: B_list[ord(b)-97] += 1

    anagram = True
    for i in range(26):
        if A_list[i] != B_list[i]: anagram = False
    answer = f"{A} & {B} are anagrams." if anagram else f"{A} & {B} are NOT anagrams."
    
    print(answer)