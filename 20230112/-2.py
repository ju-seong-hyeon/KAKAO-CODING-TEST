if __name__ == "__main__":
    str1 = "handshake"
    str2 = "shake hands"
    a = []
    b = []
    c = []
    d = []
    str1 = str1.upper()
    str2 = str2.upper()
    k = str1.split(" ")
    l = str2.split(" ")

    for i in k:
        str1 = i
        for j in (0, len(i) - 1):
            v = str1[j : j + 2]
            for k in v:
                if('A' > k or k > 'Z'):
                    break
                else:
                    a.append(v)
    for i in l:
        str1 = i
        for j in (0, len(i) - 1):
            v = str1[j : j + 2]
            for k in v:
                if('A' > k or k > 'Z'):
                    break
                else:
                    b.append(v)
    print(a)
    print(b)
    c = a+ b
    print(c)
    # for i in range(0, len(str1)-1):
    #     v = str1[i:i+2]
    #     for j in v:
    #         if('A' > j or j > 'Z'):
    #             break
    #         else:
    #             a.append(v)
    #
    # for i in range(0, len(str2)-1):
    #     v = str2[i:i + 2]
    #     for j in v:
    #         if ('A' > j or j > 'Z' or j== " "):
    #             break
    #         else:
    #             b.append(v)
    # c = a+b
    # d = []
    # for i in a:
    #     if i in b:
    #         d.append(i)
    #
    # c = set(c)
    # d = set(d)
    # v = (len(d) / len(c)) * 65536
    # print(int(v))
