from collections import defaultdict

if __name__ == "__main__":
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k  = 2
    id_dic = {}
    report_dic = defaultdict(list)
    answer = []

    report = set(report)
    report = list(report)

    for i in id_list:
        id_dic[i] = 0
        report_dic[i] = []

    for i in report:
        report_split = i.split()
        id_dic[report_split[1]] += 1

    for i in report:
        report_split = i.split()
        report_doId = report_split[0]
        report_reqId = report_split[1]

        if(id_dic[report_reqId] >= 2):
            report_dic[report_doId].append(report_reqId)

    for v in report_dic.values():
        answer.append(len(v))

    print(answer)




