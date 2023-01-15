if __name__ == "__main__":
    msg = 'ABABABABABABABAB'
    dic = dict()
    for i in range(26):
        dic[chr(65 + i)] = i + 1
    ans = []
    #print(msg)
    w = 0
    c = 0

    while(True):
        c += 1
        if(c==len(msg)):
            ans.append(dic[msg[w:c]])
            break
        if(msg[w:c+1] not in dic):
            dic[msg[w:c+1]] = len(dic) + 1
            print(msg[w:c+1])
            ans.append(dic[msg[w:c]])
            w = c

    print(ans)
    print(dic)

