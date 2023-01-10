if __name__ == "__main__":
    dartResult = "1D2S#10S"
    #S, D - 제곱 T - 3제곱
    #* - 2배, # - -2배,
    score = 0
    a_list = []
    ch_list = []
    star_list = []
    shap_list = []
    for i, v in enumerate(dartResult):
        if(v == 'S'):
            v = int(dartResult[i-1])
            if(v == 0):
                if(dartResult[i-2] == '1'):
                    a_list.append([i, 10])
            else:
                a_list.append([i, v])
        elif(v == 'D'):
            v = pow(int(dartResult[i-1]), 2)
            if(v == 0):
                if (dartResult[i - 2] == '1'):
                    a_list.append([i, 100])
            else:
                a_list.append([i, v])
        elif(v == 'T'):
            v = pow(int(dartResult[i - 1]), 3)
            if (v == 0):
                if (dartResult[i - 2] == '1'):
                    a_list.append([i, 1000])
            else:
                a_list.append([i, v])
        elif(v == '*'):
            star_list.append(i)
        elif(v == '#'):
            shap_list.append(i)
    star_cnt = len(star_list)
    shap_cnt = len(shap_list)
    print(shap_cnt)
    if(star_cnt == 2):
        fir = star_list[0]
        sec = star_list[1]
        for i in range(3):
            if(a_list[i][0] == fir-1):
                a_list[i][1] *= 4
            elif(a_list[i][0] == sec-1):
                a_list[i][1] *= 2

    elif(star_cnt == 1):
        fir = star_list[0]
        for i in range(3):
            if (a_list[i][0] == fir-1):
                a_list[i][1] *= 2
                a_list[i-1][1] *= 2

    if(shap_cnt!= 0):
        fir = shap_list[0]
        for i in range(3):
            if (a_list[i][0] == fir - 1):
                a_list[i][1] *= -1

    for i in a_list:
        score += i[1]
    print(score)
    print(a_list)