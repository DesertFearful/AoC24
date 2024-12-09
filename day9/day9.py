def preprocess(file_name):
    data, free = [], set()
    index = 0
    with open(file_name, 'r') as file:
        content = file.read().strip()
        for i, block in enumerate(content):
            for j in range(int(block)):
                if i % 2 == 0:
                    data.append(i//2)
                else:
                    data.append('.')
                    free.add((index, int(block)))
            index += int(block)
    spaces = sorted(list(free), key=lambda x: x[0])
    return data, spaces


def compact(arr):
    i, j = 0, len(arr)-1
    while i < j:
        while arr[j] == '.':
            j -= 1
        while arr[i] != '.':
            i += 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    return arr


def p1_sol(data):
    memory = compact(data)
    i, res = 0, 0
    while i < len(memory) and memory[i] != '.':
        res += memory[i] * i
        i += 1
    return res


def scan_spaces(arr):
    spaces, i = [], 0
    while i < len(arr):
        while arr[i] != '.':
            i += 1
        length = 0
        while i+length < len(arr) and arr[i+length] == '.':
            length += 1
        spaces.append((i, length))
        i += length+1
    return spaces


def compact_2(arr, spaces):
    j = len(arr)-1
    while j > 0:
        while arr[j] == '.':
            j -= 1
        length = 0
        while j-length >= 0 and arr[j-length] == arr[j]:
            length += 1

        for i in range(len(spaces)):
            if length <= spaces[i][1] and (start := spaces[i][0]) < j:
                arr[start: start+length], arr[j-length+1:j+1] = arr[j-length+1:j+1], arr[start: start+length]
                break
        spaces = scan_spaces(arr)
        j -= length
    return arr



def p2_sol(data, free):
    memory = compact_2(data, free)
    res = 0
    for i in range(len(memory)):
        if memory[i] != '.': res += memory[i] * i
    return res


if __name__ == '__main__':
    data, free = preprocess('input.txt')
    print(p1_sol(data))
    print(p2_sol(data, free))


