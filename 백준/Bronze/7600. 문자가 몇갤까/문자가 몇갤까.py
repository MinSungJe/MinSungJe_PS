while True:
    letter = input()
    if letter == '#': break
        
    upperLetter = letter.upper()
    visited = [0 for _ in range(91)]
    
    for l in upperLetter:
        if ord(l) < 65 or ord(l) > 90: continue
        if not visited[ord(l)]: visited[ord(l)] = 1

    print(sum(visited))