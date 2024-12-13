from copy import deepcopy

def preprocess(file_name):
    data =[]
    with open(file_name, 'r') as file:
        line = file.readline().strip().split()
        for x in line: data.append((int(x)))
    return data


def blink(arr):
    iter = len(arr)
    for i in range(iter):
        if arr[i] == 0:
            arr[i] = 1
        elif (length := len(str(arr[i]))) % 2 == 0:
            arr.append(arr[i] % (10 ** (length // 2)))
            arr[i] = arr[i] // (10** (length // 2))
        else:
            arr[i] *= 2024


def p1_sol(data):
    new = deepcopy(data)
    for i in range(25):
        blink(new)
    return len(new)


def digit(x):
    count = 0
    while x > 0:
        count += 1
        x //= 10
    return count


def blink_stone(stone, blink):
    if blink == 0:
        return 1
    elif (stone, blink) in memo:
        return memo[(stone, blink)]
    elif stone == 0:
        val = blink_stone(1, blink-1)
    elif (length := digit(stone)) % 2 == 0:
        first, second = stone // (10 ** (length // 2)), stone % (10 ** (length // 2))
        val = blink_stone(first, blink-1) + blink_stone(second, blink-1)
    else:
        val = blink_stone(stone*2024, blink-1)
    memo[(stone, blink)] = val
    return val


def p2_sol(data):
    res = 0
    for i in data:
        res += blink_stone(i, 75)
    return res


if __name__ == '__main__':
    data = preprocess('input.txt')
    print(p1_sol(data))
    memo ={}
    print(p2_sol(data))
