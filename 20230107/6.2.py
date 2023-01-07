def solution(new_id):
    cur_id = ""
    for i in new_id:
        if ('a' <= i <= 'z' or '0' <= i <= '9' or i == '-' or i == '_' or i == '.'):
            cur_id += i
        cur_id = cur_id.replace('..', '.')
    if (len(cur_id) >= 2):
        if (cur_id[0] == '.'):
            cur_id = cur_id[1:]
        if (cur_id[-1] == '.'):
            cur_id = cur_id[:-1]
    elif (len(cur_id) == 1 and cur_id[0] == '.'):
        cur_id = ""

    if (len(cur_id) == 0):
        cur_id = 'a'
    if (len(cur_id) >= 16):
        cur_id = cur_id[:15]
        if (cur_id[-1] == '.'):
            cur_id = cur_id[:-1]
    while (len(cur_id) <= 2):
        cur_id += cur_id[-1]
    return cur_id