Armor, ArmorIgnore = map(int, input().split())

print(1 if round(Armor * (1-(0.01*ArmorIgnore)),2) < 100 else 0)