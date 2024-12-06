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


def check_cycle(map, x, y):
    n, m = len(map), len(map[0])
    i, j = x, y
    move = '^'
    seen = set()
    while True:
        while move == '^':
            if map[i-1][j] != '#':
                i -= 1
            elif (pair := (i, j, move)) in seen:
                return True
            else:
                seen.add(pair)
                move = '>'
            if i == 0 and move == '^': return False
        while move == '>':
            if map[i][j+1] != '#':
                j += 1
            elif (pair := (i, j, move)) in seen:
                return True
            else:
                seen.add(pair)
                move = 'v'
            if j == m-1 and move == '>': return False
        while move == 'v':
            if map[i+1][j] != '#':
                i += 1
            elif (pair := (i, j, move)) in seen:
                return True
            else:
                seen.add(pair)
                move = '<'
            if i == n-1 and move == 'v': return False
        while move == '<':
            if map[i][j-1] != '#':
                j -= 1
            elif (pair := (i, j, move)) in seen:
                return True
            else:
                seen.add(pair)
                move = '^'
            if j == 0 and move == '<': return False


def p2_sol(map, x, y):
    res = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'x' and (i,j) != (x,y):
                map[i][j] = '#'
                res += 1 if check_cycle(map, x, y) else 0
                map[i][j] = 'x'
    return res


if __name__ == '__main__':
    data, x, y = preprocess('day6/input.txt')
    print(p1_sol(data, x, y))
    print(p2_sol(data, x, y))
