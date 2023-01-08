
if __name__ == "__main__":
    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]
    n = len(board)
    m = len(board[0])
    answer = 0
    sta = []

    # for i in range(n):
    #     doll = board[i][1 - 1]
    #     print(doll)

    for move in moves:
        for i in range(n):
            doll = board[i][move-1]
            if(doll != 0):
                board[i][move-1] = 0
                if(len(sta) > 1 and sta[-1] == doll):
                    sta.pop()
                    answer += 2
                    while(True):
                        if(len(sta) >= 2 and sta[-1] == sta[-2]):
                            sta.pop()
                            sta.pop()
                            answer+=2
                        else:
                            break
                else:
                    sta.append(doll)

                break

    print(answer)