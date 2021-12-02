lines = None
with open('day02/input.txt') as f:
    lines = f.readlines()

# part 1
x = 0
y = 0
for s in lines:
    cmd, _d = s.split(" ")
    d = int(_d)
    if cmd == "forward": x += d
    if cmd == "down": y += d
    if cmd == "up": y -= d

print (x * y)

# part 2
x = 0
y = 0
aim = 0
for s in lines:
    cmd, _d = s.split(" ")
    d = int(_d)
    if cmd == "forward": 
        x += d
        y += d * aim
    if cmd == "down": aim += d
    if cmd == "up": aim -= d

print (x * y)