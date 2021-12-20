scanners = []
with open('day19/input.txt') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    if line == "": 
        continue
    if line.startswith("---"): 
        scanner = []
        scanners.append(scanner)
        continue
    scanner.append(list(map(lambda s: int(s), line.split(","))))

def add(p, q):
    result = p.copy()
    for i in range(3):
        result[i] += q[i]
    return result

def sub(p, q):
    result = p.copy()
    for i in range(3):
        result[i] -= q[i]
    return result

def rot(p):
    x, y, z = p
    return [
        [ x,  y,  z], [ x,  z,  y], [ y,  x,  z], [ y,  z,  x], [ z,  x,  y], [ z,  y,  x], 
        [ x, -y,  z], [ x, -z,  y], [ y, -x,  z], [ y, -z,  x], [ z, -x,  y], [ z, -y,  x], 
        [-x,  y, -z], [-x,  z, -y], [-y,  x, -z], [-y,  z, -x], [-z,  x, -y], [-z,  y, -x], 
        [-x, -y, -z], [-x, -z, -y], [-y, -x, -z], [-y, -z, -x], [-z, -x, -y], [-z, -y, -x]
     ] 

def trans(s, r, v):
    result = []
    for p in s:
        pr = rot(p)[r]
        result.append(add(pr, v))
    return result

def count_matches(s1, s2) -> int:
    n = 0
    for p in s1:
        if p in s2:
            n += 1
    #if n > 1: print(n)
    return n

def match(s1, s2):
    for p1 in s1:
        for p2 in s2:
            p2rotations = rot(p2)
            for r in range(len(p2rotations)):
                p2r = p2rotations[r]
                v = sub(p1, p2r)
                s2x = trans(s2, r, v)
                if count_matches(s1, s2x) >= 12:
                    return (r, v)

# test
# for i in range(len(scanners)-1):
#     print(i+1, match(scanners[0], scanners[i+1]))

beacons = scanners[0].copy()
L1 = [0]
L2 = list(range(1, len(scanners)))
while len(L2) > 0:
    #for s1 in L1:
        for s2 in L2:
            print(s2)
            # m = match(scanners[s1], scanners[s2])
            m = match(beacons, scanners[s2])
            if m:
                print(s2, "*")
                r, v = m
                s2x = trans(scanners[s2], r, v)
                scanners[s2] = s2x
                for b in s2x:
                    if not b in beacons: 
                        beacons.append(b)
                L1.append(s2)
                L2.remove(s2)
                break
        #if m: break

print(len(beacons))
