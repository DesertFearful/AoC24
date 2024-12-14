import re
from copy import deepcopy


def preprocess(file_name):
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            numbers = []
            row = line.strip()
            nums = re.findall('-*\d{1,3}', row)
            for x in nums:
                if x[0] == '-':
                    numbers.append(-int(x[1:]))
                else:
                    numbers.append(int(x))
            data.append(numbers)
    return data


def simulate(arr, n, m, sec):
    x, y, dx, dy = arr[0], arr[1], arr[2], arr[3]
    for i in range(sec):
        x = (n + x + dx) % n
        y = (m + y + dy) % m

    return x, y


def p1_sol(data):
    q1, q2, q3, q4 = 0, 0, 0, 0
    for i in range(len(data)):
        x, y = simulate(data[i], 101, 103, 100)
        if x < 50 and y < 51:
            q1 += 1
        elif x > 50 and y < 51:
            q2 += 1
        elif x < 50 and y > 51:
            q3 += 1
        elif x > 50 and y > 51:
            q4 +=1 
    return q1 * q2 * q3 * q4


def create_img(data, n, m):
    loc = [['.' for i in range(n)] for j in range(m)]
    for i in range(len(data)):
        loc[data[i][1]][data[i][0]] = '1'
    res = ''
    for i in range(len(loc)):
        res += "".join(loc[i]) +'\n'
    return res
    

def p2_sol(data):
    safety, sec = float('inf'), 0
    for i in range(10000):
        q1, q2, q3, q4 = 0, 0, 0, 0
        for j in range(len(data)):
            x, y = simulate(data[j], 101, 103, 1)
            data[j][0], data[j][1] = x, y
            if x < 50 and y < 51:
                q1 += 1
            elif x > 50 and y < 51:
                q2 += 1
            elif x < 50 and y > 51:
                q3 += 1
            elif x > 50 and y > 51:
                q4 +=1
        if (score := q1*q2*q3*q4) < safety:
            safety, sec = score, i
            config = deepcopy(data)
    res = create_img(config, 101, 103)
    return res
    

if __name__ == '__main__':
    data = preprocess('day14/input.txt')
    print(p1_sol(data))
    print(p2_sol(data))