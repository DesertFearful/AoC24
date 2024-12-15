def preprocess(file_name):
    data, dir = [], []
    x, y = 0, 0
    with open(file_name, 'r') as file:
        for i, line in enumerate(file):
            elem = []
            row = line.strip()
            for j in range(len(row)):
                if '#' in row:
                    elem.append(row[j])
                    if row[j] == '@':
                        x, y = j, i
                elif row[j] == '<':
                    dir.append((-1,0))
                elif row[j] == '^':
                    dir.append((0,-1))
                elif row[j] == '>':
                    dir.append((1,0))            
                elif row[j] == 'v':
                    dir.append((0,1))
            if elem != []:
                data.append(elem)
    return data, dir, (x, y)


def move(grid, start, dir):
    x, y = start[0]+dir[0], start[1]+dir[1]
    if grid[y][x] == '.':
        grid[start[1]][start[0]], grid[y][x] = '.', '@'
        new_start = (x, y)
    elif grid[y][x] == '#':
        new_start = start
    else:
        next_x, next_y = x, y
        while grid[next_y][next_x] == 'O':
            next_x += dir[0]
            next_y += dir[1]
        if grid[next_y][next_x] == '.':
            grid[start[1]][start[0]], grid[next_y][next_x] = '.', 'O'
            grid[y][x] = '@'
            new_start = (x, y)
        else:
            new_start = start
    return grid, new_start


def create_img(arr):
    res = ''
    for i in range(len(arr)):
        res += ''.join(arr[i]) + '\n'
    return res


def p1_sol(data, moves, start):
    for m in moves:
        data, start = move(data, start, m)
    total_gps = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'O':
                total_gps += 100*i +j
    return total_gps


def double_map(data):
    grid = []
    for i in range(len(data)):
        row = []
        for j in range(len(data[i])):
            if data[i][j] == 'O':
                row.append('[')
                row.append(']')
            elif data[i][j] == '@':
                row.append('@')
                row.append('.')
            else:
                row.append(data[i][j])
                row.append(data[i][j])
        grid.append(row)
    return grid


# Function that moves boxes once it has been checked that the boxes are movable
def move_box_ver(grid, start, dir):
    '''
    start: tuple (x1, y, x2), which represents the position of the first box to be pushed
    '''
    x1, x2, y1 = start[0]+dir[0], start[2]+dir[0], start[1]+dir[1]

    # The base case: there is space in front
    if grid[y1][x1] == '.' and grid[y1][x2] == '.':
        grid[y1][x1], grid[y1][x2] = '[', ']'
        grid[start[1]][start[0]], grid[start[1]][start[2]] = '.', '.'
        return grid
    
    # If there isn't space, push recursively boxes in front of it
    while grid[y1][x1] in '[]' or grid[y1][x2] in '[]':
        if grid[y1][x1] == '[':
            grid = move_box_ver(grid, (x1, y1, x2), dir)
        else:
            if grid[y1][x1] == ']':
                grid = move_box_ver(grid, (x1-1, y1, x1), dir)
            if grid[y1][x2] == '[':
                grid = move_box_ver(grid, (x2, y1, x2+1), dir)

    # Final push after space in front has been cleared
    grid[y1][x1], grid[y1][x2] = '[', ']'
    grid[start[1]][start[0]], grid[start[1]][start[2]] = '.', '.'
    return grid


def can_move_ver(grid, start, dir):
    x1, x2, y1 = start[0]+dir[0], start[2]+dir[0], start[1]+dir[1]
    if grid[y1][x1] == '#' or grid[y1][x2] == '#':
        return False
    elif grid[y1][x1] == grid[y1][x2] == '.':
        return True
    
    while grid[y1][x1] in '[]' or grid[y1][x2] in '[]':
        if grid[y1][x1] == '[':
            if not can_move_ver(grid, (x1, y1, x2), dir):
                return False
        else:
            if grid[y1][x1] == ']':
                if not can_move_ver(grid, (x1-1, y1, x1), dir):
                    return False
            if grid[y1][x2] == '[':
                if not can_move_ver(grid, (x2, y1, x2+1), dir):
                    return False
        return True
    

def can_move_hor(grid, start, dir):
    x = start[0]
    while grid[start[1]][x] in '[]':
        x += dir[0]
    if grid[start[1]][x] == '#':
        return False
    return True


def move_box_hor(grid, start, dir):
    x = start[0]
    while grid[start[1]][x] in '[]':
        x += dir[0]
    while grid[start[1]][x-dir[0]] in '[]':
        grid[start[1]][x], grid[start[1]][x-dir[0]] = grid[start[1]][x-dir[0]], grid[start[1]][x]
        x -= dir[0]
    return grid
    

def move_p2(data, start, dir):
    x, y = start[0]+dir[0], start[1]+dir[1]
    if data[y][x] == '.':
        data[y][x], data[start[1]][start[0]] = '@', '.'
        start = (x, y)
    elif data[y][x] in '[]':
        if dir[1] != 0:
            if data[y][x] == '[' and can_move_ver(data, (x, y, x+1), dir):
                data = move_box_ver(data, (x, y, x+1), dir)
                data[y][x], data[start[1]][start[0]] = '@', '.'
                start = (x, y)
            elif data[y][x] == ']' and can_move_ver(data, (x-1, y, x), dir):
                data = move_box_ver(data, (x-1, y, x), dir)
                data[y][x], data[start[1]][start[0]] = '@', '.'
                start = (x, y)
        else:
            if can_move_hor(data, (x,y), dir):
                data = move_box_hor(data, (x, y), dir)
                data[y][x], data[start[1]][start[0]] = '@', '.'
                start = (x, y)
    return data, start


def p2_sol(data, moves, start):
    for m in moves:
        data, start = move_p2(data, start, m)
    total_gps = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '[':
                total_gps += 100*i +j
    return total_gps


if __name__ == '__main__':
    data, moves, start = preprocess('day15/input.txt')
    new_data = double_map(data)
    new_start = (2*start[0], start[1])
    print(p1_sol(data, moves, start))
    print(p2_sol(new_data, moves, new_start))