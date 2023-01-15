

if __name__ == "__main__":
    dic = {}
    msg = 'KAKAO'
    w = 0
    c = 0
    ans = []
    for i in range(26):
        dic[chr(65+i)] = i+1

    while(True):
        c += 1
        if(c == len(msg)):
            ans.append(dic[msg[w:c]])
            break
        if(msg[w:c+1] not in dic):
            ans.append(dic[msg[w:c]])
            dic[msg[w:c+1]] = len(dic)+1
            w = c
    print(dic)
    print(ans)