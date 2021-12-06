lines = None
with open('day06/input.txt') as f:
    lines = f.readlines()

line = lines[0]
arr = list(map(lambda s: int(s), line.split(",")))

for day in range(80):
    for i in range(len(arr)):
        arr[i] -= 1
        if arr[i] == -1: 
            arr[i] = 6
            arr.append(8)

print(len(arr))
