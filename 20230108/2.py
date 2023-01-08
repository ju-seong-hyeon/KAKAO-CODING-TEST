
if __name__ == "__main__":
    numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    hand = "left"
    # result = "LRLLRRLLLRR"
    answer = ''

    loc = {1:(1,1), 2:(1,2), 3:(1,3), 4:(2,1), 5:(2,2),
           6:(2,3), 7:(3,1), 8:(3,2), 9:(3,3), 0:(4,2)}
    cur_left = (4,1)
    cur_right = (4,3)

    for i in numbers:
        if (i == 1 or i == 4 or i == 7):
            answer += 'L'
            cur_left = loc[i]
        elif (i == 3 or i == 6 or i == 9):
            answer += 'R'
            cur_right = loc[i]
        else:
            loc_but = loc[i]
            dis_left = (abs(loc_but[0] - cur_left[0]) + abs(loc_but[1] - cur_left[1]))
            dis_right = (abs(loc_but[0] - cur_right[0]) + abs(loc_but[1] - cur_right[1]))
            if(i == 0):
                print(dis_left, dis_right)
            if (dis_left < dis_right):
                cur_left = loc[i]
                answer += 'L'
            elif (dis_left > dis_right):
                cur_right = loc[i]
                answer += 'R'
            else:
                if (hand == 'right'):
                    cur_right = loc[i]
                    answer += 'R'
                else:
                    cur_left = loc[i]
                    answer += 'L'
    print(answer)