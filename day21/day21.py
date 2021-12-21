player = 0
# pos = [4, 8] # sample
pos = [7, 3]
score = [0, 0]
dice = 0
rolls = 0

while True:
    q = 0
    for i in range(3):
        rolls += 1  
        dice += 1
        q += dice
        if dice == 100: dice = 0
    
    pos[player] = 1 + (pos[player] + q - 1) % 10
    score[player] += pos[player]

    print(player + 1, q, pos[player], score[player])

    if score[player] >= 1000: break

    player = (player + 1) % 2

player = (player + 1) % 2
print (rolls * score[player])