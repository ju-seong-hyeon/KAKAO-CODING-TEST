
def solution(msg):
    ans = []
    dic = {}

    for i in range(26):
        dic[chr(65 + i)] = i+1

    w, c = 0, 0
    while True:
        c += 1
        if c == len(msg):
            ans.append(dic[msg[w:c]])
            break
        if msg[w:c+1] not in dic:
            dic[msg[w:c+1]] = len(dic) + 1
            ans.append(dic[msg[w:c]])
            w = c
    return ans
if __name__ == "__main__":
    print(solution('KAKAO'))