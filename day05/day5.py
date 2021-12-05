lines = None
with open('day05/input.txt') as f:
    lines = f.readlines()

arr=[]
for y in range(1000):
    a = []
    for x in range(1000): a.append(0)
    arr.append(a)

count = 0
for line in lines:
    x1, y1, x2, y2 = map(lambda s: int(s), line.replace(" -> ", ",").split(","))

    if x1 == x2:
        x = x1
        if y1 > y2: y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            arr[x][y] += 1
            if arr[x][y] == 2: count += 1
    elif y1 == y2:
        y = y1
        if x1 > x2: x1, x2 = x2, x1
        for x in range(x1, x2 + 1):
            arr[x][y] += 1
            if arr[x][y] == 2: count += 1
    else: # part 2
        if x1 > x2: 
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        q = -1 if y1 > y2 else 1
        x = x1
        y = y1
        for i in range(0, x2 - x1 + 1):
            arr[x + i][y + q * i] += 1
            if arr[x + i][y + q * i] == 2: count += 1

print(count)