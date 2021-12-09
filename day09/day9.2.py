def parse():
    with open('day09/input.txt') as f:
        lines = f.readlines()

    arr = []
    for line in lines:
        a = []
        for c in line.strip():
            a.append(int(c))
        arr.append(a)
        
    return arr

arr = parse()
h = len(arr)
w = len(arr[0])

def wave(xx: int, yy: int) -> int:
    n = 0
    q = [ [yy, xx] ]
    while len(q) > 0:
        y, x = q.pop(0)
        if arr[y][x] == -1: continue
        arr[y][x] = -1
        n += 1
        if x > 0 and arr[y][x-1] != 9 and arr[y][x-1] != -1: 
            q.append([y, x-1])
        if y > 0 and arr[y-1][x] != 9 and arr[y-1][x] != -1:
            q.append([y-1, x])
        if x < w-1 and arr[y][x+1] != 9 and arr[y][x+1] != -1:
            q.append([y, x+1])
        if y < h-1 and arr[y+1][x] != 9 and arr[y+1][x] != -1:
            q.append([y+1, x])

    return n

basins = []
for y in range(h):
    for x in range(w):
        if arr[y][x] != -1 and arr[y][x] != 9:
            size = wave(x, y)
            basins.append(size)
             
basins = sorted(basins, reverse=True)
product = 1
for i in range(3):
    product *= basins[i]
print(product)