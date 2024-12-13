from collections import defaultdict, deque


def preprocess(file_name):
    data, starts = [], []
    with open(file_name, 'r') as file:
        for i, line in enumerate(file):
            nums = []
            row = line.strip()
            for j in range(len(row)):
                if (x := int(row[j])) == 0:
                    starts.append((i,j))
                nums.append(x)
            data.append(nums)
    return data, starts


def create_graph(grid):
    n, m = len(grid), len(grid[0])
    graph = defaultdict(list)
    direction = [(1,0), (-1,0), (0,1), (0,-1)]
    for i in range(n):
        for j in range(m):
            for dir in direction:
                x, y = i+dir[0], j+dir[1]
                if 0 <= x < n and 0 <= y < m and grid[i][j] == grid[x][y]-1:
                    graph[(i, j)].append((x, y))
    return graph


def score(start, graph, grid):
    res = 0
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            res += 1 if grid[node[0]][node[1]] == 9 else 0
        for next in graph[node]:
            if next not in visited:
                queue.append(next)
    return res


def p1_sol(data, starts):
    res = 0
    graph = create_graph(data)
    for s in starts:
        res += score(s, graph, data)
    return res


def rating(start, graph, grid):
    res = 0
    stack = [start]

    while stack:
        node = stack.pop()
        for next in graph[node]:
            stack.append(next)
        res += 1 if grid[node[0]][node[1]] == 9 else 0
    return res


def p2_sol(data, starts):
    res = 0
    graph = create_graph(data)
    for s in starts:
        res += rating(s, graph, data)
    return res


if __name__ == '__main__':
    data, starts = preprocess('input.txt')
    print(p1_sol(data, starts))
    print(p2_sol(data, starts))