lines = None
with open('day04/input.txt') as f:
    lines = f.readlines()

def score(number: int, board: int) -> int:
    sum = 0
    for i in range(board * 6, board * 6 + 5):
        for n in arr[i]: sum += n
        arr[i] = []
    print(f"b:{board} n:{number} sum:{sum} score:{number*sum}")

def check(board: int) -> bool:
    rows = list(range(board * 6, board * 6 + 5))
    cols = list(range(5))
    for r in range(board * 6, board * 6 + 5):
        for c in range(5):
            if arr[r][c] != 0:
                if r in rows: rows.remove(r)
                if c in cols: cols.remove(c)
    return len(rows) > 0 or len(cols) > 0

numbers = lines[0].split(",")
numbers = list(map(lambda s: int(s), numbers))
lines.pop(0)
lines.pop(0)

arr = []
for line in lines:
    q = line.split(" ")
    q = list(filter(lambda s: s.strip() != "", q))
    arr.append(list(map(lambda s: int(s), q)))

for number in numbers:
    for i in range(len(arr)):
        a = arr[i]
        if number in a:
            j = a.index(number)
            if j >= 0: a[j] = 0
            if check(i // 6): score(number, i // 6)
