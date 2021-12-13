with open('day13/input.txt') as f:
    lines = f.readlines()

points = []
for line in lines:
    x, y = line.split(",")
    points.append( (int(x), int(y)) )

def distinct(l: list) -> list:
    result = []
    for item in l:
        if not item in result:
            result.append(item)
    return result

def foldY(yy: int):
    global points
    for i in range(len(points)):
        x, y = points[i]
        if y > yy:
            points[i] = (x, 2 * yy - y)
    points = distinct(points)
    print(len(points))

def foldX(xx: int):
    global points
    for i in range(len(points)):
        x, y = points[i]
        if x > xx:
            points[i] = (2 * xx - x, y)
    points = distinct(points)
    print(len(points))

def show():
    xx = 0
    yy = 0
    for p in points:
        x, y = p
        if x > xx: xx = x
        if y > yy: yy = y

    for y in range(yy+1):
        for x in range(xx+1):
            if (x, y) in points:
                print("@", end="")
            else:
                print(" ", end="") 
        print("")  

# sample.txt:
# foldY(7)
# foldX(5)
# print()

foldX(655)
foldY(447)
foldX(327)
foldY(223)
foldX(163)
foldY(111)
foldX(81)
foldY(55)
foldX(40)
foldY(27)
foldY(13)
foldY(6)
show()