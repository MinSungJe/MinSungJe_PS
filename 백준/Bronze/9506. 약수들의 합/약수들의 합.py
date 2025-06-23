while True:
    n = int(input())
    if n == -1: break

    answer = []
    for i in range(1, int(n**(1/2))+1):
        if n % i != 0: continue

        if i * i == n: answer.append(i)
        else:
            answer.append(i)
            answer.append(n // i)
    
    answer.sort()
    if sum(answer[:-1]) == answer[-1]: print(f"{answer[-1]} = {' + '.join(map(str, answer[:-1]))}")
    else: print(f"{answer[-1]} is NOT perfect.")