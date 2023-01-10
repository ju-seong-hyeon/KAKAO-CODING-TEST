if __name__ == "__main__":
    n = ''
    score = []
    dartResult = "1D2S#10S"
    dic = {"S" :1, "D":2, "T":3}
    dartResult = dartResult.replace("10", "X")
    sta = []
    for i in dartResult:
        if('0' <= i <='9' or i == 'X'):
            sta.append(10 if i=='X' else int(i))
        elif i in ['S', 'D', 'T']:
            num = sta.pop()
            sta.append(num ** dic[i])
        elif i == '#':
            sta[-1] *= -1
        elif i == '*':
            num = sta.pop()
            if( len(sta)):
                sta[-1] *= 2
            sta.append(2 * num)

    print(sum(sta))
