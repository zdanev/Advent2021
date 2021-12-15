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

def calc_risk(i: int, j: int) -> int:
    min = big
    if i > 0 and risk[i-1][j] != 0 and risk[i-1][j] + arr[i][j] < min: min = risk[i-1][j] + arr[i][j]
    if j > 0 and risk[i][j-1] != 0 and risk[i][j-1] + arr[i][j] < min: min = risk[i][j-1] + arr[i][j]
    if i < n-1 and risk[i+1][j] != 0 and risk[i+1][j] + arr[i][j] < min: min = risk[i+1][j] + arr[i][j]
    if j < n-1 and risk[i][j+1] != 0 and risk[i][j+1] + arr[i][j] < min: min = risk[i][j+1] + arr[i][j]
    return min

arr = read_input()
n = len(arr)
risk = []
init()
risk[0][0] = arr[0][0]

q = True
while q:
    q = False
    min = big
    for i in range(n):
        for j in range(n):
            if risk[i][j] == 0:
                q = True
                r = calc_risk(i, j)
                if r > 0 and r < min: min = r
    for i in range(n):
        for j in range(n):
            if risk[i][j] == 0:
                r = calc_risk(i, j)
                if r == min: risk[i][j] = min

print(risk[n-1][n-1] - risk[0][0])
