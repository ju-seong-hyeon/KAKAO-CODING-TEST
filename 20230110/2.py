def binary(v):
    global binary_v
    if(v>0):
        binary(v//2)
        if (v % 2 == 0):
            binary_v += " "
        else:
            binary_v += "#"

if __name__ == "__main__":
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    a = []
    b = []
    c = []

    for i in arr1:
        binary_v = ""
        binary(i)

        for i in range(len(binary_v), n):
            binary_v = " " + binary_v
        # binary_v = binary_v[:-1]
        a.append(binary_v)

    for i in arr2:
        binary_v = ""
        binary(i)

        for i in range(len(binary_v), n):
            binary_v = " " + binary_v
        # binary_v = binary_v[:-1]
        b.append(binary_v)

    print(a)
    print(b)

    for i in range(n):
        v1 = a[i]
        v2 = b[i]
        v = ""
        for j in range(n):
            if(v1[j] == '#' or v2[j] =='#'):
                v += '#'
            else:
                v += ' '
        c.append(v)
    print(c)