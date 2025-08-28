T = int(input())
for _ in range(T):
    HP, MP, ATK, DEF, HP_, MP_, ATK_, DEF_ = map(int, input().split())

    final_HP, final_MP, final_ATK, final_DEF = max(1, HP+HP_), max(1, MP+MP_), max(0, ATK+ATK_), DEF+DEF_

    answer = 1 * final_HP + 5 * final_MP + 2 * final_ATK + 2 * final_DEF
    print(answer)