if __name__ == "__main__":
    n = 5
    stages = [2,1,2,6,4,3,3]
    res = {}
    le_stages = len(stages)
    for i in range(1, n+1):
        if le_stages != 0:
            count = stages.count(i)
            res[i] = count / le_stages
            le_stages -= count
        else:
            res[i] = 0
    res = sorted(res, key = lambda x: res[x], reverse=True)
    print(res)