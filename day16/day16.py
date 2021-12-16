with open('day16/input.txt') as f:
    lines = f.readlines()
    packet = lines[0]

def hex2bin(hex: str) -> str:
    b = ""
    for c in hex:
        ci = int(c, 16)
        b += (bin(ci)[2:]).zfill(4)
    return b

def bin2int(b: str) -> int:
    return int(b, 2)

def parse(packet: str):
    print("hex: " + packet)
    packet_bin = hex2bin(packet)
    print("bin: " + packet_bin)
    parse_packet(packet_bin)

def parse_packet(q: str) -> int:
    print("parse packet: " + q)
    global sum_ver

    ver = q[0:3]
    veri = bin2int(ver)
    sum_ver += veri
    print("ver: " + ver + " " + str(veri))
    
    type = q[3:6]
    typei = bin2int(type)
    print("type: " + type + " " + str(typei))

    if typei == 4:
        len = parse_literal(q[6:])
    else: 
        len = parse_operator(q[6:])

    return len + 6

def parse_literal(q: str) -> int:
    print("parse literal: " + q)
    literal = ""
    i = 0
    while (True):
        i += 1
        s = q[0:5]
        literal += s[1:]
        q = q[5:]
        if s[0] == "0": break
    print("literal: " + literal)
    return i * 5

def parse_operator(q: str):
    print("parse operator: " + q)
    i = q[0]
    print("i: " + i)
    len = 1

    if i == "0": # by length
        l = q[1:16]
        li = bin2int(l)
        print("l: " + l + " " + str(li))
        len += 15
        sub = q[16:16 + li]
        print("sub: " + sub)
        while li > 0:
            subl = parse_packet(sub)
            sub = sub[subl:]
            len += subl
            li -= subl
    else: # by count
        n = q[1:12]
        ni = bin2int(n)
        print("n: " + n + " " + str(ni))
        len += 11
        sub = q[12:]
        for i in range(ni):
            print(f"sub {i+1}/{ni}")
            l = parse_packet(sub)
            sub = sub[l:]
            len += l

    return len

sum_ver = 0

# literal
#parse("D2FE28")

# operator (2 subpackets: literals)
# parse("38006F45291200")

# op(3 li)
# parse("EE00D40C823060")

# op(op(op(li))) -> 16
# parse("8A004A801A8002F478")

# op(op(2 li), op(2 li)) -> 12
# parse("620080001611562C8802118E34")

# op(op(2 li), op(2 li)) -> 23
# parse("C0015000016115A2E0802F182340")

# op(op(op(5 li))) -> 31
# parse("A0016C880162017C3686B18A3D4780")

parse(packet)

print(sum_ver)