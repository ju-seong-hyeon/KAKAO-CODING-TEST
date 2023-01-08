if __name__ == "__main__":
    n = 5
    stages = [2,1,2,6,4,3,3]
    # result = [3,4,2,1,5]
    stages.sort()
    loseRate = []
    res = []
    a_max = 0

    for i in range(1, n+1):
        if(i in stages):
            loseRate.append([i, stages.count(i) / len(stages)])
            while(i in stages):
                stages.remove(i)
            # print(stages)
        else:
            loseRate.append([i, 0])
    # print(loseRate)
    loseRate.sort(key=lambda x:(x[1], x[0]), reverse=True)
    print(loseRate)