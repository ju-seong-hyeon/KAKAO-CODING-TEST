msg = 'KAKAO'
def dfs(lev, ret):
    global ans
    global dic
    if(lev == len(msg)):
        return
    else:
        val = msg[lev : ret+1]
        if(val in dic):
            ans.append(dic.index(val)+1)
            dfs(lev)
        else:
            dic.append(val)
            ans.append(dic.index(val)+1)
            dfs(lev+1, ret)


def sulution(msg):
    dic = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
           'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    ans = []
    dfs(0, 1)


    
