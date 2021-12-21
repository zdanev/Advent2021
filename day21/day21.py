player = 0
# pos = [4, 8] # sample
pos = [7, 3] # input
score = [0, 0]
dice = 0
turn = 0

while True:
    roll = 0
    for i in range(3):
        turn += 1  
        dice += 1
        roll += dice
        if dice == 100: dice = 0
    
    pos[player] = 1 + (pos[player] + roll - 1) % 10
    score[player] += pos[player]

    print(player + 1, roll, pos[player], score[player])

    if score[player] >= 1000: break

    player = (player + 1) % 2

player = (player + 1) % 2
print (turn * score[player])