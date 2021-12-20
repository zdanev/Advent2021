LIGHT = "#"
DARK = "."
iterations = 50
padding = iterations * 2

with open('day20/input.txt') as f:
    lines = f.readlines()
    map = lines[0].strip()
    lines.pop(0)
    lines.pop(0)

image = []
h = len(lines)
w = len(lines[0].strip())

def blank():
    q = []
    for i in range(2 * padding + h):
        qq = []
        for j in range(2 * padding + w):
            qq.append(DARK)
        q.append(qq)
    return q

image = blank()
for r in range(h):
    for c in range(w):
        image[r + padding][c + padding] = lines[r][c]

def dump():
    for row in range(len(image)):
        for col in range(len(image[0])):
            print(image[row][col], end="")
        print()
    print()

# dump()
for q in range(iterations):
    buf = blank()
    for row in range(1, len(image) -1):
        for col in range(1, len(image[0]) -1):
            s = ""
            for rr in range(row-1, row+2):
                for cc in range(col-1, col+2):
                    s += "0" if image[rr][cc] == DARK else "1"
            s10 = int(s, 2)
            buf[row][col] = map[s10]
    image = buf
    # dump()

count = 0
for row in range(padding // 2, len(image) - padding // 2):
    for col in range(padding // 2, len(image) - padding // 2):
        if image[row][col] == LIGHT:
            count += 1

print(count)
