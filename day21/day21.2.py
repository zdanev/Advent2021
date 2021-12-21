from collections import defaultdict

dice = defaultdict(int)
for d1 in range(1, 4):
    for d2 in range(1, 4):
        for d3 in range(1, 4):
            dice[d1 + d2 + d3] += 1

player = 0
p1 = 7
p2 = 3
s1 = 0
s2 = 0

universes = defaultdict(int)
universes[(p1, p2, s1, s2)] = 1

q = True
while q:
    q = False
    next = defaultdict(int)

    for uni in universes:
        p1, p2, s1, s2 = uni
        if max(s1, s2) < 21:
            q = True
            for roll in dice:
                p1, p2, s1, s2 = uni
                if player == 0:
                    p1 = 1 + (p1 + roll - 1) % 10
                    s1 += p1
                else:
                    p2 = 1 + (p2 + roll - 1) % 10
                    s2 += p2

                next[(p1, p2, s1, s2)] += dice[roll] * universes[uni]
        else:
            next[(p1, p2, s1, s2)] += universes[uni]

    universes = next
    player = (player + 1) % 2

wins1 = 0
wins2 = 0
for uni in universes:
    p1, p2, s1, s2 = uni
    if s1 >= 21: wins1 += universes[uni]
    if s2 >= 21: wins2 += universes[uni]

print(max(wins1, wins2))
