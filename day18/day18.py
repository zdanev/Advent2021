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

    def explode(self):
        q = self.traverse()

        ex = None
        for p in q:
            if p.can_explode():
                ex = p
                break

        if ex is not None:
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

    def add(self, p):
        return Pair(self, p)

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

### TESTS ###

print(Parser("[1,[2,3]]").parse())

# [[1,9],[8,5]] + [9,[8,7]] -> [[[1,9],[8,5]],[9,[8,7]]]
print(Parser("[[1,9],[8,5]]").parse().add(Parser("[9,[8,7]]").parse()))

# [[[[[9,8],1],2],3],4] -> [[[[0,9],2],3],4]
p = Parser("[[[[[9,8],1],2],3],4]").parse()
print(p)
p.explode()
print(p)

# [7,[6,[5,[4,[3,2]]]]] -> [7,[6,[5,[7,0]]]]
p = Parser("[7,[6,[5,[4,[3,2]]]]]").parse()
print(p)
p.explode()
print(p)

# [[6,[5,[4,[3,2]]]],1] -> [[6,[5,[7,0]]],3]
p = Parser("[[6,[5,[4,[3,2]]]],1]").parse()
print(p)
p.explode()
print(p)

# [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]] -> [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
p = Parser("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]").parse()
print(p)
p.explode()
print(p)

# [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] -> [[3,[2,[8,0]]],[9,[5,[7,0]]]]
p = Parser("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]").parse()
print(p)
p.explode()
print(p)
