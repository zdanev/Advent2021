lines = None
with open('day03/input.txt') as f:
    lines = f.readlines()

# Part 1

w = len(lines[0].strip())
n = len(lines)
counts = []
for i in range(w):
    counts.append(0)

for s in lines:
    for i in range(w):
        if s[i] == "1": counts[i] += 1

gamma = 0 # most common bit at position
epsilon = 0 # least common bit at position

for i in range(w):
    gamma *= 2
    epsilon *= 2
    if counts[i] > 500:
        gamma += 1
    else:
        epsilon += 1

print(gamma * epsilon)

# Part 2

l = lines.copy()
for i in range(w):
    c0 = 0
    c1 = 0
    for s in l:
        if s[i] == "1": c1 += 1 
        else: c0 += 1
    
    q = "1" if c1 >= c0 else "0"
    l = list(filter(lambda x: x[i] == q, l))
    if len(l) == 1: break

o2 = int(l[0], 2)

l = lines.copy()
for i in range(w):
    c0 = 0
    c1 = 0
    for s in l:
        if s[i] == "1": c1 += 1 
        else: c0 += 1
    
    q = "0" if c0 <= c1 else "1"
    l = list(filter(lambda x: x[i] == q, l))
    if len(l) == 1: break

co2 = int(l[0], 2)

print (o2 * co2)
