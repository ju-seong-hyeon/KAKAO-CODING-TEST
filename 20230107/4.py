

if __name__ == "__main__":
    survey = ["TR", "RT", "TR"]
    choices = [7, 1, 3]
    score = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    n = len(survey)
    mbti = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0,'N':0}
    answer = ""
    #
    # for i in survey:
    #     for j in range(len(i)):
    #         mbti[i[j]] = 0

    for i in range(n):
        fir = survey[i][0]
        sec = survey[i][1]
        choice = choices[i]
        if(choices[i] < 4):
            mbti[fir] += score[choice]
            # mbti[survey[0]]
        else:
            mbti[sec] += score[choice]

    if(mbti['R'] < mbti['T']):
        answer += 'T'
    elif(mbti['R'] == mbti['T']):
        answer += 'R'
    else:
        answer += 'R'

    if (mbti['C'] < mbti['F']):
        answer += 'F'
    elif (mbti['C'] == mbti['F']):
        answer += 'C'
    else:
        answer += 'C'
    if (mbti['J'] < mbti['M']):
        answer += 'M'
    elif (mbti['J'] == mbti['M']):
        answer += 'J'
    else:
        answer += 'J'
    if (mbti['A'] < mbti['N']):
        answer += 'N'
    elif (mbti['A'] == mbti['N']):
        answer += 'A'
    else:
        answer += 'A'
    print(answer)

