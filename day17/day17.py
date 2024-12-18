import re

def preprocess(file_name):
    reg = []
    with open(file_name, 'r') as file:
        for line in file:
            num = re.findall('\d+', line)
            if len(num) == 1:
                reg.append(int(num[0]))
            else:
                instr = [int(x) for x in num]
    return reg, instr


def combo(operand):
    if operand in {0,1,2,3}:
        return operand
    elif operand == 4:
        return regA
    elif operand == 5:
        return regB
    elif operand == 6:
        return regC


def adv(operand):
    global regA
    denom = 2**combo(operand)
    regA =  regA // denom


def bxl(operand):
    global regB
    regB = regB ^ operand


def bst(operand):
    global regB
    regB = combo(operand) % 8


def jnz(operand):
    if regA != 0:
        return operand
    return


def bxc(operand):
    global regB
    regB = regB ^ regC


def out(operand):
    res = combo(operand) % 8
    return res


def bdv(operand):
    global regB
    denom = 2 ** combo(operand)
    regB = regA // denom


def cdv(operand):
    global regC
    denom = 2 ** combo(operand)
    regC = regA // denom


def p1_sol(instr):
    res, i = [], 0
    while i < len(instr):
        opcode, operand = instr[i], instr[i+1]
        if opcode == 0:
            adv(operand)
        elif opcode == 1:
            bxl(operand)
        elif opcode == 2:
            bst(operand)
        elif opcode == 3 and jnz(operand) != None:
            i = jnz(operand)
            continue
        elif opcode == 4:
            bxc(operand)
        elif opcode == 5:
            res.append(out(operand))
        elif opcode == 6:
            bdv(operand)
        elif opcode == 7:
            cdv(operand)
        i += 2
    return res


def check(instr, a):
    b, c = 0, 0
    p = 0
    while a != 0 and p < len(instr):
        c = a >> ((a & 7) ^ 7)
        b = (a & 7) ^ c
        a = a >> 3
        if instr[p] != (b & 7):
            return False
        p += 1
    return a == 0 and p == len(instr)


def find(instr):
    i = len(instr)-1
    cand_a = 0
    while i > -1:
        for j in range(8):
            a  = (cand_a << 3) | j
            if check(instr[i:], a):
                break
        i -= 1
        cand_a = a
    return cand_a



if __name__ == '__main__':
    reg, instr = preprocess('input.txt')
    regB, regC = reg[1], reg[2]
    # print(check(instr, 117440))
    res = find(instr)
    print(res)
    regA, regB, regC = res, reg[1], reg[2]
    print(p1_sol(instr))
    regB, regC = reg[1], reg[2]
    print(check(instr, res))
