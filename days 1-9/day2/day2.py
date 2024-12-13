def preprocess(file_name):
    input = []
    with open(file_name, 'r') as file:
        for line in file:
            row = [int(x) for x in line.split()]
            input.append(row)
    return input


def check(arr):
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        if arr[1] - arr[0] > 0 and not (1 <= diff <= 3):
            return False
        elif arr[1] - arr[0] < 0 and not (-3 <= diff <= -1):
            return False
        elif arr[1] -  arr[0] == 0:
            return False
    return True


def p1_sol(num):
    res = 0
    for i in range(len(num)):
        res += 1 if check(num[i]) else 0
    return res


def check_tolerate(arr):
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        if arr[1] - arr[0] > 0 and not (1 <= diff <= 3):
            return True if (check(arr[:i] + arr[i+1:]) or check(arr[:i-1] + arr[i:])) else False
        elif arr[1] - arr[0] < 0 and not (-3 <= diff <= 1):
            return True if (check(arr[:i] + arr[i+1:]) or check(arr[:i-1] + arr[i:])) else False
        elif arr[1] - arr[0] == 0:
            return True if (check(arr[1:]) or check(arr[:1] + arr[2:])) else False
    return True


def p2_sol(num):
    res = 0
    for i in range(len(num)):
        res += 1 if check_tolerate(num[i]) else 0
    return res


if __name__ == '__main__':
    nums = preprocess('input.txt')
    print(p1_sol(nums))
    print(p2_sol(nums))