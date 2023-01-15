

if __name__ == "__main__":
    recode = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    res = []
    id = {}
    for i in recode:
        i = i.split(' ')
        if i[0] == 'Change':
            id[i[1]] = i[2]
        elif i[0] == 'Enter':
            id[i[1]] = i[2]
    print(id)
    for i in recode:
        i = i.split(' ')
        if(i[0] == 'Enter'):
            res.append('%s님이 들어왔습니다.' %id[i[1]])
        elif(i[0] == 'Leave'):
            res.append('%s님이 나갔습니다.' %id[i[1]])

    print(res)
