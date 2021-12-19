from day18.day18 import Parser

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

# [[[[4,3],4],4],[7,[[8,4],9]]] + [1,1]
print(Parser("[[[[4,3],4],4],[7,[[8,4],9]]]").parse().add(Parser("[1,1]").parse()))

# magnitude
print(Parser("[[1,2],[[3,4],5]]").parse().magnitude()) # 143
print(Parser("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]").parse().magnitude()) # 1384
print(Parser("[[[[1,1],[2,2]],[3,3]],[4,4]]").parse().magnitude()) # 445
print(Parser("[[[[3,0],[5,3]],[4,4]],[5,5]]").parse().magnitude()) # 791
print(Parser("[[[[5,0],[7,4]],[5,5]],[6,6]]").parse().magnitude()) # 1137
print(Parser("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]").parse().magnitude()) # 3488
