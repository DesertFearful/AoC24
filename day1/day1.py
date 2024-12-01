def day1p1(file_name):
    nums1, nums2, res = [], [], 0

    with open(file_name, 'r') as file:
        for line in file:
            row = line.split()
            nums1.append(int(row[0]))
            nums2.append(int(row[1]))

    nums1.sort(), nums2.sort()
    
    for i in range(len(nums1)):
        res += abs(nums1[i] - nums2[i])

    print(res)

if __name__ == '__main__':
    day1p1('day1/input.txt')