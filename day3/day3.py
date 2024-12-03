import re


def preprocess(pattern, file_name='input.txt'):
    """
    Extracts all matches for a given regex pattern from a file.
    """
    res = []
    with open(file_name, 'r') as file:
        for line in file:
            res += re.findall(pattern, line)
    return res


def p1_sol(arr):
    """
    Computes the sum of products of numbers extracted from an array of patterns.
    """
    res = 0
    for i in range(len(arr)):
        numbers = re.findall(r'\d{1,3}', arr[i])
        a, b = int(numbers[0]), int(numbers[1])
        res += a * b
    return res


def p2_sol(arr):
    """
    Computes the sum of products of numbers, handling control patterns ('do()', 'don't()').
    """
    stop, res = False, 0
    for i in range(len(arr)):
        if arr[i] == 'do()':
            stop = False
        elif arr[i] == "don't()":
            stop = True
        elif not stop:
            numbers = re.findall(r'\d{1,3}', arr[i])
            a, b = int(numbers[0]), int(numbers[1])
            res += a * b
    return res

if __name__ == '__main__':
    real_1 = preprocess(r'mul\(\d{1,3},\d{1,3}\)')
    real_2 = preprocess(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)')
    print(p1_sol(real_1))
    print(p2_sol(real_2))