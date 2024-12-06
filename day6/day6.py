def preprocess(file_name):
    map = []
    x, y = 0, 0
    with open(file_name, 'r') as file:
        for i, line in enumerate(file):
            row = list(line.strip())
            if '^' in line:
                x, y = i, row.index('^')
                row = row[:y] + ['x'] + row[y+1:]
            map.append(row)
    return map, x, y

def p1_sol(map, x, y):
    n, m = len(map), len(map[0])
    i, j = x, y
    move = '^'
    count = 1
    while True:
        while move == '^':
            if map[i-1][j] != '#':
                if map[i-1][j] == '.':
                    count += 1
                    map[i-1][j] = 'x'
                i -= 1
            else:
                move = '>'
            if i == 0 and move == '^': return count
        while move == '>':
            if map[i][j+1] != '#':
                if map[i][j+1] == '.':
                    count += 1
                    map[i][j+1] = 'x'
                j += 1
            else:
                move = 'v'
            if j == m-1 and move == '>': return count
        while move == 'v':
            if map[i+1][j] != '#':
                if map[i+1][j] == '.':
                    count += 1
                    map[i+1][j] = 'x'
                i += 1
            else:
                move = '<'
            if i == n-1 and move == 'v': return count
        while move == '<':
            if map[i][j-1] != '#':
                if map[i][j-1] == '.':
                    count += 1
                    map[i][j-1] = 'x'
                j -= 1
            else:
                move = '^'
            if j == 0 and move == '<': return count
    return count



map_, x, y = preprocess('input.txt')
print(map_, x, y)
print(p1_sol(map_, x, y))
