from collections import defaultdict

with open('day22/input.txt') as f:
    lines = f.readlines()

dic = defaultdict(int)
for line in lines:
    line = line.replace("on ", "1,").replace("off", "0,").replace("..", ",") \
        .replace("x=", "").replace("y=", "").replace("z=", "")
    
    q, x1, x2, y1, y2, z1, z2 = map(int, line.split(","))

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            for z in range(z1, z2 + 1):
                dic[(x, y, z)] = q

count = 0
for key in dic:
    count += dic[key]

print(count)
