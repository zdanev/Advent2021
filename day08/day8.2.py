lines = None
with open('day08/input.txt') as f:
    lines = f.readlines()

# a is superset of b
def ss(a: str, b: str) -> bool:
    for c in b:
        if not c in a: return False
    return True

def subract(a: str, b: str) -> str:
    for x in b:
        a = a.replace(x, "")
    return a

sum = 0
for line in lines:
    input, output = line.split("|")

    # process input
    s = input.strip().split(" ")
    one = ""
    seven = ""
    four = ""
    for x in s:
        if len(x) == 2: one = x
        if len(x) == 3: seven = x
        if len(x) == 4: four = x
    q = subract(four, one)

    # process output
    s = output.strip().split(" ")
    num = 0
    for x in s:
        num *= 10
        x = x.strip()
        l = len(x)
        if l == 2: num += 1
        elif l == 3: num += 7
        elif l == 4: num += 4
        elif l == 5:
            if ss(x, seven): num += 3
            elif ss(x, q): num += 5
            else: num += 2
        elif l == 6:
            if ss(x, four): num += 9
            elif ss(x, seven): num += 0 
            else: num += 6
        elif l == 7: 
            num += 8

    sum += num

print(sum)
