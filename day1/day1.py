def preprocess(file_name):
    a, b = [], []

    with open(file_name, 'r') as file:
        for line in file:
            row = line.split()
            a.append(int(row[0]))
            b.append(int(row[1]))
    
    return a, b


def day1p1(a, b):
    a.sort(), b.sort()
    res = 0
    for i in range(len(a)):
        res += abs(a[i] - b[i])
    print(res)


def day1p2(a, b):
    table = {}
    res = 0
    for i in range(len(b)):
        table[b[i]] = 1 + table.get(b[i], 0)
    for i in range(len(a)):
        if a[i] in table:
            res += a[i] * table[a[i]]
    print(res)


if __name__ == '__main__':
    nums1, nums2 = preprocess('day1/input.txt')
    day1p1(nums1, nums2)
    day1p2(nums1, nums2)