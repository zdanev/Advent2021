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
for i in range(40):
    print(i+1)
    # print(f"{i+1}: {poly}")
    poly = grow(poly)

counts = {}
for p in poly:
    if p in counts:
        counts[p] += 1
    else:
        counts[p] = 1

counts = sorted(counts.values())
print(counts[-1] - counts[0])
