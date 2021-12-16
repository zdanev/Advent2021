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

packet_bin = ""
index = 0
def get_token(len: int) -> str:
    global index
    token = packet_bin[index:index+len]
    index += len
    return token

def get_int_token(len: int) -> int:
    return bin2int(get_token(len))

sum_ver = 0
def parse(packet: str):
    global packet_bin, index, sum_ver
    print("hex", packet)
    packet_bin = hex2bin(packet)
    index = 0
    sum_ver = 0
    # print("bin: ", packet_bin)

    result = parse_packet()

    print()
    print("sum_ver", sum_ver)
    print("result", result)

def get_aggregate(type: int) -> str:
    if type == 0: aggregate = "+"
    elif type == 1: aggregate = "*"
    elif type == 2: aggregate = "min"
    elif type == 3: aggregate = "max"
    elif type == 5: aggregate = "gt"
    elif type == 6: aggregate = "lt"
    elif type == 7: aggregate = "eq"
    return aggregate

def cacl_aggregate(aggregate: str, data: list) -> int:
    if aggregate == "+":
        return sum(data)
    if aggregate == "*":
        result = 1
        for x in data: result *= x
        return result
    if aggregate == "min":
        result = data[0]
        for x in data: 
            if x < result: result = x
        return result
    if aggregate == "max":
        result = data[0]
        for x in data: 
            if x > result: result = x
        return result
    if aggregate == "gt":
        if data[0] > data[1]: return 1
        else: return 0
    if aggregate == "lt":
        if data[0] < data[1]: return 1
        else: return 0
    if aggregate == "eq":
        if data[0] == data[1]: return 1
        else: return 0

def parse_packet() -> int:
    global sum_ver
    sum_ver += get_int_token(3)

    type = get_int_token(3)
    if type == 4:
        result = parse_literal()
    else:
        aggregate = get_aggregate(type)
        print("(" + aggregate + " ", end="")
        results = parse_operator()
        print(")", end="") 
        result = cacl_aggregate(aggregate, results)
    
    return result

def parse_literal() -> int:
    flag = True
    result = 0
    while flag:
        flag = get_int_token(1) == 1
        token = get_int_token(4)
        result = result * 16 + token
    print(f"[{result}]", end="")
    return result

def parse_operator():
    result = []

    id = get_int_token(1)
    if id == 0: # by length
        len = get_int_token(15)
        target_index = index + len
        while index < target_index:
            sub = parse_packet()
            result.append(sub)
    else: # by count
        n = get_int_token(11)
        for i in range(n):
            sub = parse_packet()
            result.append(sub)

    return result

# [2021]=2021 sum_ver=6
parse("D2FE28")

# (+ [1][2])=3 sum_ver=14
parse("C200B40A82")

# (lt [10][20])=1 sum_ver=9
parse("38006F45291200")

# (max [1][2][3])=3 sum_ver=14
parse("EE00D40C823060")

# (min(min(min(15))))=15 sum_ver=16
parse("8A004A801A8002F478")

# (+ (+ [10][11]) (+ [12][13]))=46 sum_ver=12
parse("620080001611562C8802118E34")

# (+ (+ [10][11]) (+ [12][13]))=46 sum_ver=23
parse("C0015000016115A2E0802F182340")

# (+ (+ (+ [6][6][12][15][15])))=54 sum_ver=31
parse("A0016C880162017C3686B18A3D4780")

parse(packet)
