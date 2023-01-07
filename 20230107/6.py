if __name__ == "__main__":
    new_id = "...!@BaT#*..y.abcdefghijklm"
    new_id = new_id.lower()
    cur_id = ""
    for i in new_id:
        # print(nei, end = " ")
        if('a'<=i<='z' or '0'<=i<='9' or i=='-' or i=='_' or i=='.'):
            # print(i)
            cur_id += i
        cur_id = cur_id.replace('..', '.')

    if (len(cur_id) >= 2):
        if (cur_id[0] == '.'):
            cur_id = cur_id[1:]
        if (cur_id[-1] == '.'):
            cur_id = cur_id[:-1]
    elif(len(cur_id) ==1 and cur_id[0] == '.'):
        cur_id = ""
    if(len(cur_id) == 0):
        cur_id = 'a'
    if(len(cur_id)>=16):
        cur_id = cur_id[:15]
        if(cur_id[-1] == '.'):
            cur_id = cur_id[:-1]
    while(len(cur_id)<=2):
        cur_id += cur_id[-1]
    print(cur_id)
