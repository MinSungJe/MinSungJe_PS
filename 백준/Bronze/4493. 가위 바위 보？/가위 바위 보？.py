T = int(input())
for _ in range(T):
    N = int(input())
    player1 = 0
    player2 = 0
    for _ in range(N):
        turn1, turn2 = input().split()
        if turn1 == 'R':
            if turn2 == 'S': player1 += 1
            if turn2 == 'P': player2 += 1
        if turn1 == 'S':
            if turn2 == 'R': player2 += 1
            if turn2 == 'P': player1 += 1
        if turn1 == 'P':
            if turn2 == 'R': player1 += 1
            if turn2 == 'S': player2 += 1
    
    if player1 > player2: print('Player 1')
    if player1 == player2: print('TIE')
    if player1 < player2: print('Player 2')