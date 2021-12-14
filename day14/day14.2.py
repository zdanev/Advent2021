with open('day14/input.txt') as f:
    lines = f.readlines()

dic = {}
for line in lines:
    a, b = line.strip().split(" -> ")
    dic[a] = b

def grow(poly: str) -> str:
    result = ""
    for i in range(len(poly) - 1):
        q = poly[i:i+2]
        result += poly[i] +dic[q]
    result += poly[-1]
    return result

# poly = "NNCB" # sample
poly = "CKFFSCFSCBCKBPBCSPKP"

pairs = {}
for i in range(len(poly) - 1):
    p = poly[i:i+2]
    if p in pairs:
        pairs[p] += 1
    else:
        pairs[p] = 1

def grow():
    global pairs
    newpairs = {}
    for p in pairs:
        q = dic[p]
        n = pairs[p]
        p1 = p[0] + q
        if p1 in newpairs: 
            newpairs[p1] += n
        else:
            newpairs[p1] = n
        p2 = q + p[1]
        if p2 in newpairs: 
            newpairs[p2] += n
        else:
            newpairs[p2] = n
    pairs = newpairs

for i in range(40):
    print(i+1)
    grow()

counts = {}
for p in pairs:
    n = pairs[p]
    p1 = p[0]
    if p1 in counts:
        counts[p1] += n
    else:
        counts[p1] = n
    p2 = p[1]
    if p2 in counts:
        counts[p2] += n
    else:
        counts[p2] = n

counts[poly[0]] += 1
counts[poly[-1]] += 1

counts = sorted(counts.values())
print((counts[-1] - counts[0]) // 2)
