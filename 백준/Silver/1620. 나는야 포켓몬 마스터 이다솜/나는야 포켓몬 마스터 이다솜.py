import sys
def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
pokemon = {}
for i in range(1,N+1):
    pokemon[str(i)] = input()
reveredPokemon = {v:k for k,v in pokemon.items()}

for i in range(M):
    index = input()
    if index in pokemon.keys(): print(pokemon[index])
    if index in reveredPokemon.keys(): print(reveredPokemon[index])