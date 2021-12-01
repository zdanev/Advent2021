lines = None
with open('input.txt') as f:
    lines = f.readlines()

# part 1
prev = int(lines[0])
inc = 0
for n in lines:
    x = int(n)
    if x > prev: inc += 1
    prev = x

print(inc)

# part 2
inc = 0
prev = int(lines[0]) + int(lines[1]) + int(lines[2])
for i in range(3, len(lines)):
    a = int(lines[i-3])
    b = int(lines[i])
    x = prev - a + b
    if x > prev: inc += 1
    prev = x

print(inc)