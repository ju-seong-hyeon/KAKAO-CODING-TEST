from collections import Counter

if __name__ == "__main__":
    str1 = "FRANCE"
    str2 = "french"
    str1 = str1.lower()
    str2 = str2.lower()
    a = []
    b = []
    for i in range(len(str1)-1):
        if(str1[i].isalpha() and str1[i+1].isalpha()):
            a.append(str1[i] + str1[i+1])

    for i in range(len(str2)-1):
        if(str2[i].isalpha() and str2[i+1].isalpha()):
            b.append(str2[i] + str2[i+1])

    Counter1 = Counter(a)
    Counter2 = Counter(b)

    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())
    print(inter)
    print(union)
    value = 65536
    if(len(union) == 0 and len(inter) == 0):
        print(65536)
    else:
        print(int(len(inter) / len(union) * 65536))
