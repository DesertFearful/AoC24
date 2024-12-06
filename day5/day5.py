from collections import defaultdict

def preprocess(file_name):
    data, rules = [], defaultdict(list)
    with open(file_name, 'r') as file:
        for line in file:
            if '|' in line:
                nums = line.strip().split('|')
                rules[int(nums[0])].append(int(nums[1]))
            elif len(line) != 1:
                data.append([int(x) for x in line.strip().split(',')])
    return data, rules


def check_row(arr, rules):
    seen = set()
    for i in range(len(arr)):
        if arr[i] in rules:
            for x in rules[arr[i]]:
                if x in seen:
                    return False
        seen.add(arr[i])
    return True


def p1_sol(data, rules):
    res = 0
    for i in range(len(data)):
        if check_row(data[i], rules):
            res += data[i][len(data[i])//2]
    return res


def correct_row(arr, rules):
    seen = set()
    for i in range(len(arr)):
        if arr[i] in rules:
            for x in rules[arr[i]]:
                if x in seen:
                    j = arr.index(x)
                    arr[j], arr[i] = arr[i], arr[j]
                    return
        seen.add(arr[i])
    return


def p2_sol(data, rules):
    res = 0
    for i in range(len(data)):
        check = check_row(data[i], rules)
        if not check:
            while not check:
                correct_row(data[i], rules)
                check = check_row(data[i], rules)
            res += data[i][len(data[i])//2]
    return res

if __name__ == '__main__':
    data, rules = preprocess('day5/input.txt')
    print(p1_sol(data, rules))
    print(p2_sol(data, rules))