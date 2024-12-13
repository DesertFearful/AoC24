import math
import re

def preprocess(file_name):
    equations = []
    with open(file_name, 'r') as file:
        content = file.readlines()
        for i in range(0, len(content), 4):
            nums = []
            for j in range(3):
                numbers = re.findall('\d{1,6}', content[i+j])
                for x in numbers: nums.append(int(x))
            equations.append(nums)
    return equations


def solve(arr):
    det = arr[0]*arr[3] - arr[1]*arr[2]
    A = (arr[4]*arr[3] - arr[5]*arr[2]) / det
    B = (arr[0]*arr[5] - arr[1]*arr[4]) / det
    if A == math.floor(A) and B == math.floor(B):
        return [int(A), int(B)]
    return []


def p1_sol(data):
    tokens = 0
    for i in range(len(data)):
        if res := solve(data[i]):
            A, B = res[0], res[1]
            tokens += A*3 + B
    return tokens


def preprocess_part2(file_name):
    equations = []
    with open(file_name, 'r') as file:
        content = file.readlines()
        for i in range(0, len(content), 4):
            nums = []
            for j in range(3):
                numbers = re.findall('\d{1,6}', content[i+j])
                for x in numbers:
                    if j == 2:
                        nums.append(int(x)+10**13)
                    else:
                        nums.append(int(x))
            equations.append(nums)
    return equations


if __name__ == '__main__':
    data1 = preprocess('input.txt')
    data2 = preprocess_part2('input.txt')
    print(p1_sol(data1))
    print(p1_sol(data2))