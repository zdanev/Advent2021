lines = None
with open('day06/input.txt') as f:
    lines = f.readlines()

line = lines[0]
arr = list(map(lambda s: int(s), line.split(",")))

arr2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(arr)):
    arr2[arr[i]] += 1

for day in range(256):
    zeros = arr2[0]
    for i in range(1, 9):
        arr2[i-1] = arr2[i]
    arr2[6] += zeros
    arr2[8] = zeros

sum = 0
for i in range(9): sum += arr2[i]
print(sum)