with open('day10/input.txt') as f:
    lines = f.readlines()

def match(c):
    if c == ')': return '('
    if c == ']': return '['
    if c == '}': return '{'
    if c == '>': return '<'
    if c == '(': return ')'
    if c == '[': return ']'
    if c == '{': return '}'
    if c == '<': return '>'

def score(c):
    if c == ')': return 3
    if c == ']': return 57
    if c == '}': return 1197
    if c == '>': return 25137

def score2(c):
    if c == ')': return 1
    if c == ']': return 2
    if c == '}': return 3
    if c == '>': return 4

# part 1

sum = 0
for line in lines:
    stack = []

    for c in line.strip():
        if c in '([{<': 
            stack.append(c)
        else:
            d = stack.pop()
            if not match(c) == d:
                sum += score(c)

print(sum)

# part 2

scores = []
for line in lines:
    stack = []
    for c in line.strip():
        if c in '([{<': 
            stack.append(c)
        else:
            if len(stack) == 0: 
                break # incomplete
            d = stack.pop()
            if not match(c) == d:
                stack = []
                break # illegal

    score = 0
    for _ in range(len(stack)):
        x = stack.pop()
        score = score * 5 + score2(match(x))
    if score > 0:
        scores.append(score)

scores = sorted(scores)
print(scores[len(scores) // 2])
