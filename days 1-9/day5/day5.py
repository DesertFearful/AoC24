from collections import defaultdict


def preprocess(file_name):
    rules, data = defaultdict(list), []
    with open(file_name, 'r') as file:
        for line in file:
            if '|' in line:
                nums = line.strip().split('|')
                rules[int(nums[0])].append(int(nums[1]))
            elif line != '\n':
                arr = [int(x) for x in line.strip().split(',')]
                data.append(arr)
    return rules, data


def p1_sol(rules, data):
    res = 0
    for i in range(len(data)):
        invalid, n = False, len(data[i])
        seen = set()
        for j in range(n):
            if data[i][j] in rules:
                for x in rules[data[i][j]]:
                    if x in seen:
                        invalid = True
                        break
            if invalid:
                break
            seen.add(data[i][j])
        if not invalid:
            res += data[i][n//2]
    return res


# def correct_order(rules, arr):
#     seen = set()
#     corrected = []
#     for i in range(len(arr)):
#         if arr[i] in rules:
#             for x in rules[arr[i]]:
#                 if x in seen:




rules, data = preprocess('input.txt')
print(p1_sol(rules, data))