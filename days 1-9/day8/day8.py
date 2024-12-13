from collections import defaultdict


def preprocess(file_name):
    data = []
    freq = defaultdict(list)
    with open(file_name, 'r') as file:
        for i, row in enumerate(file):
            data.append(list(row.strip()))
            for j in range(len(row)):
                if row[j].isalnum():
                    freq[row[j]].append((i, j))
    return data, freq


def antinodes(a, b, n, m):
    xa, ya, xb, yb = a[0], a[1], b[0], b[1]
    dx, dy = xb - xa, yb - ya

    x1, x2 = xa - dx, xb + dx
    y1, y2 = ya - dy, yb + dy
    res = []
    if 0 <= x1 and 0 <= y1 <= m-1:
        res.append((x1, y1))
    if x2 <= n-1 and 0 <= y2 <= m-1:
        res.append((x2, y2))
    return res


def p1_sol(freq, n, m):
    unique = set()
    for letter in freq:
        for i in range(len(freq[letter])):
            for j in range(i+1, len(freq[letter])):
                res = antinodes(freq[letter][i], freq[letter][j], n, m)
                for r in res: unique.add(r)
    return len(unique)


def antinodes_line(a, b, n, m):
    xa, ya, xb, yb = a[0], a[1], b[0], b[1]
    dx, dy = xb - xa, yb - ya
    res = []
    while 0 <= xa and 0 <= ya <= m-1:
        res.append((xa, ya))
        xa -= dx
        ya -= dy
    while xb <= n-1 and 0 <= yb <= m-1:
        res.append((xb, yb))
        xb += dx
        yb += dy
    return res


def p2_sol(freq, n, m):
    unique = set()
    for letter in freq:
        for i in range(len(freq[letter])):
            for j in range(i+1, len(freq[letter])):
                res = antinodes_line(freq[letter][i], freq[letter][j], n, m)
                for r in res: unique.add(r)
    return len(unique)
    

if __name__ == '__main__':
    data, freq = preprocess('day8/test.txt')
    print(p1_sol(freq, len(data), len(data[0])))
    print(p2_sol(freq, len(data), len(data[0])))