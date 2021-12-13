with open('day12/input.txt') as f:
    lines = f.readlines()

routes = {}
for line in lines:
    a, b = line.strip().split("-")
    if a in routes: 
        routes[a] += [b]
    else:
        routes[a] = [b]
    if b in routes:
        routes[b] += [a]
    else:
        routes[b] = [a]

def step(q: list, flag: bool):
    global count
    a = q[-1]
    if not a in routes: return
    rs = routes[a]
    for r in rs:
        if r == "end": 
            count += 1
            print(q)
            continue
        if r == "start": continue
        if (r[0].isupper() or flag or not r in q):
            ff = flag
            if r[0].islower() and r in q: 
                ff = False
            qq = q.copy()
            qq += [r]
            step(qq, ff)

count = 0
step(['start'], True)
print(count)
