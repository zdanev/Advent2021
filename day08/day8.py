lines = None
with open('day08/input.txt') as f:
    lines = f.readlines()

count = 0
for line in lines:
    input, output = line.split("|")
    s = output.strip().split(" ")
    for x in s:
        l = len(x.strip()) 
        if l != 5 and l != 6: count += 1

print(count)
