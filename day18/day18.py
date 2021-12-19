class Pair:
    a = None
    b = None
    level = 0
    
    def __init__(self, a, b = None):
        self.a = a
        self.b = b

    def is_pair(self):
        return self.b is not None

    def is_literal(self):
        return self.b is None

    def traverse(self, level = 1) -> list:
        self.level = level
        if self.is_literal():
            return [self]
        else:
            aa = self.a.traverse(level + 1)
            bb = self.b.traverse(level + 1)
            aa.append(self)
            aa.extend(bb)
            return aa

    def can_explode(self):
        return self.level > 4 \
            and self.is_pair() \
            and self.a.is_literal() \
            and self.b.is_literal()

    def explode(self) -> bool:
        q = self.traverse()

        ex = None
        for p in q:
            if p.can_explode():
                ex = p
                break

        if ex is None: return False

        q.remove(ex.a)
        q.remove(ex.b)

        prev = None
        next = None
        for x in q:
            if x.is_literal() and next is not None:
                x.a += next
                break
            if x == ex:
                next = ex.b.a
                if prev is not None:
                    prev.a += ex.a.a
            if x.is_literal(): 
                prev = x

        ex.a = 0
        ex.b = None
        return True

    def split(self) -> bool:
        q = self.traverse()
        for x in q:
            if x.is_literal() and x.a >= 10:
                x.b = Pair(x.a - x.a // 2)
                x.a = Pair(x.a // 2)
                return True
        return False

    def reduce(self):
        # while (self.explode() or self.split()): pass
        while True:
            # print(self)
            if self.explode(): continue
            if self.split(): continue
            break

    def add(self, p):
        result = Pair(self, p)
        result.reduce()
        return result

    def magnitude(self) -> int:
        if self.is_literal():
            return self.a
        else:
            return 3 * self.a.magnitude() + 2 * self.b.magnitude()

    def __str__(self) -> str:
        if self.is_literal():
            return str(self.a)
        else:
            return "[" + str(self.a) + "," + str(self.b) + "]"

class Parser:
    s = None
    index = 0

    def __init__(self, s: str) -> None:
        self.s = s

    def parse(self) -> Pair:
        self.index = 0
        return self.__parse_pair()

    def __get_token(self) -> str:
        token = self.s[self.index]
        self.index += 1
        return token

    def __parse_pair(self):
        token = self.__get_token()
        if token == "[":
            a = self.__parse_pair()
            if self.__get_token() != ",": raise Exception()
            b = self.__parse_pair()
            if self.__get_token() != "]": raise Exception()
            return Pair(a, b)
        else:
            return Pair(int(token))

with open('day18/input.txt') as f:
    lines = f.readlines()

sum = None
for line in lines:
    n = Parser(line).parse()
    if sum is None:
        sum = n
    else:
        sum = sum.add(n)
print(sum.magnitude())

max = 0
for i in range(len(lines)):
    for j in range(len(lines)):
        a = Parser(lines[i]).parse()
        b = Parser(lines[j]).parse()
        m = a.add(b).magnitude()
        if m > max: max = m
print(max)
