lines = None
with open('day09/input.txt') as f:
    lines = f.readlines()

arr = []

for line in lines:
    a = []
    for c in line.strip():
        a.append(int(c))
    arr.append(a)

h = len(arr)
w = len(arr[0])

sum = 0
for x in range(w):
    for y in range(h):
        if (x == w-1 or arr[y][x] < arr[y][x + 1])  \
            and (x == 0 or arr[y][x] < arr[y][x-1]) \
            and (y == 0 or arr[y][x] < arr[y-1][x]) \
            and (y == h-1 or arr[y][x] < arr[y+1][x]):
                sum += arr[y][x] + 1
             
print(sum)