from collections import defaultdict

with open('day22/input.txt') as f:
    lines = f.readlines()

dic = defaultdict(int)
i = 0
for line in lines:
    i += 1
    print(i)
    line = line.replace("on ", "1,").replace("off", "0, ").replace("..", ",") \
        .replace("x=", "").replace("y=", "").replace("z=", "")
    
    q,x1,x2,y1,y2,z1,z2=line.split(",")

    for x in range(int(x1), int(x2) + 1):
        for y in range(int(y1), int(y2) + 1):
            for z in range(int(z1), int(z2) + 1):
                dic[(x, y, z)] = int(q)

count = 0
for key in dic:
    count += dic[key]

print(count)
