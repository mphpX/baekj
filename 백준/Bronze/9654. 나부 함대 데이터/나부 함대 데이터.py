ships = [
    ["N2 Bomber",     "Heavy Fighter",  "Limited",   21],
    ["J-Type 327",    "Light Combat",   "Unlimited", 1],
    ["NX Cruiser",    "Medium Fighter", "Limited",   18],
    ["N1 Starfighter","Medium Fighter", "Unlimited", 25],
    ["Royal Cruiser", "Light Combat",   "Limited",   4]
]

print(f"{'SHIP NAME':<15}{'CLASS':<15}{'DEPLOYMENT':<11}{'IN SERVICE':<10}")

for ship in ships:
    print(f"{ship[0]:<15}{ship[1]:<15}{ship[2]:<11}{ship[3]:<10}")
