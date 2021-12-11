def read_input():
    with open('day11/input.txt') as f:
        lines = f.readlines()

    arr = []
    for line in lines:
        a = []
        for c in line.strip():
            a.append(int(c))
        arr.append(a)
        
    return arr

def dump():
    for a in arr:
        for b in a:
            print(b, end=" ")
        print()
    print()

def init():
    global f
    f = []
    for i in range(n):
        ff = []
        for j in range(n):
            ff.append(False)
        f.append(ff)

def reset():
    for i in range(n):
        for j in range(n):
            f[i][j] = False

def all():
    for i in range(n):
        for j in range(n):
            if not f[i][j]: return False
    return True

flashes = 0
f = []
def flash(i, j):
    global flashes
    global f
    f[i][j] = True
    flashes += 1
    for ii in range(max(0, i-1), min(i+2, n)):
        for jj in range(max(0, j-1), min(j+2, n)):
            arr[ii][jj] += 1

def step():
    global f
    reset()

    for i in range(n):
        for j in range(n):
            arr[i][j] += 1

    q = True
    while q:
        q = False
        for i in range(n):
            for j in range(n):
                if not f[i][j] and arr[i][j] > 9:
                    q = True
                    flash(i, j)

    for i in range(n):
        for j in range(n):
            if arr[i][j] > 9: arr[i][j] = 0

arr = read_input()
n = len(arr)
init()
dump()

for s in range(1000):
    step()
    # dump()
    if all(): 
        print(s+1)
        break

print(flashes)
