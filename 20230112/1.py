if __name__ == "__main__":
    #users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
    #emoticons = [1300, 1500, 1600, 4900]
    #result = [4, 13860]
    users = [[40, 10000], [25, 10000]]
    emoticons = [7000, 9000]
    result = []
    score = 0
    cnt = 0
    for i in users:
        per = i[0]
        money = i[1]
        v = 0

        for j in emoticons:
            v += int((j * (100 - per) / 100))

        if (money >= v):
            score += money
            cnt += 1
        else:
            score += v

    result.append(cnt)
    result.append(score)
    print(result)