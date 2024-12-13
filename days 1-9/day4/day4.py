def preprocess(file_name):
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            row = list(line.strip('\n'))
            data.append(row)
    return data


def check(arr):
    count = 0
    if len(arr) < 4:
        return count
    for i in range(len(arr)):
        if i < len(arr)-3 and arr[i:i+4] in [['X','M','A','S'], ['S','A','M','X']]:
            count += 1
    return count


def cols(data):
    cols = []
    for i in range(len(data[0])):
        column = []
        for j in range(len(data)):
            column.append(data[j][i])
        cols.append(column)
    return cols


def diag_1(data):
    n, m = len(data), len(data[0])
    diagonals = []
    for i in range(m):
        j, diag = 0, []
        while j+i < m and j < n:
            diag.append(data[j][j+i])
            j += 1
        diagonals.append(diag)
        if i > 0:
            diag, j = [], i
            while j-i < m and j < n:
                diag.append(data[j][j-i])
                j += 1
            diagonals.append(diag)
    return diagonals


def diag_2(data):
    n, m = len(data), len(data[0])
    diagonals = []
    for i in range(n):
        j, diag = 0, []
        while n-1-j-i >= 0 and j < m:
            diag.append(data[n-1-j-i][j])
            j += 1
        diagonals.append(diag)
        if i > 0:
            j, diag = i, []
            while n-1-j+i >= 0 and j < m:
                diag.append(data[n-1-j+i][j])
                j += 1
            diagonals.append(diag)
    return diagonals


def collect_3x3(data):
    boxes = []
    for i in range(len(data)-2):
        for j in range(len(data)-2):
            box = []
            for k in range(9):
                box.append(data[i+k//3][j+k%3])
            boxes.append(box)
    return boxes


def p1_sol(data):
    rows = data
    columns = cols(data)
    secondary_diag = diag_1(data)
    main_diag = diag_2(data)
    res = 0
    for r in rows:
        res += check(r)
    for c in columns:
        res += check(c)
    for d in main_diag:
        res += check(d)
    for d in secondary_diag:
        res += check(d)
    return res


def p2_sol(data):
    count = 0
    boxes = collect_3x3(data)
    for b in boxes:
        corners = set([b[0], b[2], b[6], b[-1]])
        if b[4] == 'A' and b[0] != b[-1] and b[2] != b[6] and corners == {'S','M'}:
            count += 1
    return count


if __name__ == '__main__':
    data = preprocess('input.txt')
    print(p1_sol(data))
    print(p2_sol(data))

