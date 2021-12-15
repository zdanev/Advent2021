big = 9999999

def read_input():
    with open('day15/input.txt') as f:
        lines = f.readlines()

    arr = []
    for line in lines:
        a = []
        for c in line.strip():
            a.append(int(c))
        arr.append(a)
        
    return arr

def init():
    global risk
    risk = []
    for i in range(n):
        r = []
        for j in range(n):
            r.append(0)
        risk.append(r)

def get_risk(i: int, j: int) -> int:
    n = len(arr)
    ii = i % n
    jj = j % n
    risk = 1 + (arr[ii][jj] + i // n + j // n - 1) % 9
    return risk

def dump():
    for i in range(n):
        for j in range(n):
            print(get_risk(i, j), end="")
        print()

def calc_risk(i: int, j: int) -> int:
    min = big
    if i >= n or j >= n: return big
    rij = get_risk(i, j) 
    if i > 0 and risk[i-1][j] != 0 and risk[i-1][j] + rij < min: min = risk[i-1][j] + rij
    if j > 0 and risk[i][j-1] != 0 and risk[i][j-1] + rij < min: min = risk[i][j-1] + rij
    if i < n-1 and risk[i+1][j] != 0 and risk[i+1][j] + rij < min: min = risk[i+1][j] + rij
    if j < n-1 and risk[i][j+1] != 0 and risk[i][j+1] + rij < min: min = risk[i][j+1] + rij
    return min

arr = read_input()
n = len(arr) * 5
risk = []
init()
risk[0][0] = arr[0][0]
# dump()

edge = [ (0, 0) ]
while risk[n-1][n-1] == 0:
    min = big
    for p in edge:
        i, j = p
        if i+1 < n and risk[i+1][j] == 0:
            r = calc_risk(i+1, j)
            if r < min: min = r
        if j+1 < n and risk[i][j+1] == 0:
            r = calc_risk(i, j+1)
            if r < min: min = r
    for p in edge:
        i, j = p
        if i+1 < n and risk[i+1][j] == 0:
            r = calc_risk(i+1, j)
            if r == min: 
                risk[i+1][j] = r
                edge.append( (i+1, j) )
        if j+1 < n and risk[i][j+1] == 0:
            r = calc_risk(i, j+1)
            if r == min: 
                risk[i][j+1] = r
                edge.append( (i, j+1) )
    for p in edge:
        i, j = p
        if (i+1 < n and risk[i+1][j] == 0) or (j+1 < n and risk[i][j+1] == 0):
            pass
        else:
            edge.remove(p)

print(risk[n-1][n-1] - risk[0][0])
