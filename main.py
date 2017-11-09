
def convert(i):
    if i == 0:
        return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i /= 2
    return s


def equalize(a, b):
    if len(a) > len(b):
        for i in range(0, len(a) - len(b)):
            b.insert(0, 0)
    elif len(a) < len(b):
        for i in range(0, len(b) - len(a)):
            a.insert(0, 0)
    return a, b


def sum(a, b, ctr):
    out = ''

    if ctr > 0:
        if a[-1] + b[-1] == 2:
            out = '1'
        elif a[-1] + b[-1] == 0:
            out = '1'
            ctr -= 1
        else:
            out = '0'
    else:
        if a[-1] + b[-1] == 2:
            out = '0'
            ctr += 1
        elif a[-1] + b[-1] == 0:
            out = '0'
        else:
            out = '1'
    return out, ctr


def sum_check(a, b):
    ctr = 0
    out = []
    n = len(a)
    for i in range(n):
        if i != 0:
            a = a[:-1]
            b = b[:-1]

        new_out, ctr = sum(a, b, ctr)
        out.append(new_out)

    out.append(str(ctr))
    return out


def add(a, b):
    a = [int(x) for x in a]
    b = [int(x) for x in b]

    a, b = equalize(a, b)

    print('Result: ' + ''.join(sum_check(a, b)[::-1]))


print "Please select your first number"

in1 = input(">> ")
print "Please select your second number"
in2 = input(">> ")

bin1 = convert(int(in1))
bin2 = convert(int(in2))

add(bin1, bin2)
