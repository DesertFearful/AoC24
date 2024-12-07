def preprocess(file_name):
    targets = []
    nums = []
    with open(file_name, 'r') as file:
        for line in file:
            row = line.strip().split(" ")
            targets.append(int(row[0][:-1]))
            nums.append([int(x) for x in row[1:]])
    return targets, nums


def match(target, arr):
    if len(arr) == 0:
        return target == 0
    return match(target-arr[-1], arr[:-1]) or match(target/arr[-1], arr[:-1])


def p1_sol(targets, nums):
    res = 0
    for i in range(len(targets)):
        res += targets[i] if match(targets[i], nums[i]) else 0
    return res


def match_modif(target, arr):
    if len(arr) == 0:
        return target == 0
    count, last = 0, arr[-1]
    while last > 0:
        last //= 10
        count += 1
    return (match_modif(target-arr[-1], arr[:-1]) or 
            match_modif(target/arr[-1], arr[:-1]) or 
            match_modif((target-arr[-1])/(10**count), arr[:-1]))


def p2_sol(targets, nums):
    res = 0
    for i in range(len(targets)):
        res += targets[i] if match_modif(targets[i], nums[i]) else 0
    return res


if __name__ == '__main__':
    targets, nums = preprocess('day7/input.txt')
    print(p1_sol(targets, nums))
    print(p2_sol(targets, nums))