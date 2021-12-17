def launch(vx: int, vy: int, x1: int, x2: int, y1: int, y2: int):
    x, y = 0, 0
    max_y = 0
    while x <= x2 and y >= y2:
        # print(x, y, vx, vy)
        if y > max_y: max_y = y
        if x1 <= x <= x2 and y1 >= y >= y2: return True, max_y
        x += vx
        y += vy        
        if vx > 0: vx -= 1
        elif vx < 0: vx += 1
        vy -= 1

    return False, 0

# print(launch(7, 2, 20, 30, -5, -10))

def find_max(x1: int, x2: int, y1: int, y2: int):
    max_y = 0
    count = 0
    for vx in range(0, 500):
        for vy in range(-500, 500):
            hit, max = launch(vx, vy, x1, x2, y1, y2)
            if hit: count += 1
            if hit and max > max_y: 
                max_y = max
    print(max_y)
    print(count)

# find_max(20, 30, -5, -10)

find_max(248, 285, -56, -85)
